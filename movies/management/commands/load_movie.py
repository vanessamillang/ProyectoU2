
import os
import environ
import requests
import psycopg2
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Loads a movie, assuming the database is empty"

    def handle(self, *args, **options):
        env = environ.Env()
        environ.Env.read_env()

        self.stdout.write(self.style.SUCCESS('API_KEY: ' + env('API_KEY')))
        self.stdout.write(self.style.SUCCESS('API_TOKEN: ' + env('API_TOKEN')))

        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {env('API_TOKEN')}"
        }

        movie_id = 76344
        movie_info_url = f'https://api.themoviedb.org/3/movie/{movie_id}?language=en-US'
        credits_url = f'https://api.themoviedb.org/3/movie/{movie_id}/credits?language=en-US'

        # Realiza solicitudes para obtener información de la película y su elenco/equipo
        r = requests.get(movie_info_url, headers=headers)
        movie_data = r.json()

        r = requests.get(credits_url, headers=headers)
        credits = r.json()

        # Conectar a la base de datos PostgreSQL
        conn = psycopg2.connect(
            dbname="django_bootstrap",
            user="ubuntu",
            password="bugalox3",
            host="127.0.0.1",
            port="5432"
        )
        cursor = conn.cursor()

        insert_movie_query = "INSERT INTO movies_movie(id, title, overview, release_date, budget, revenue, poster_path) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(insert_movie_query, (movie_data['id'], movie_data['title'], movie_data['overview'], movie_data['release_date'], movie_data['budget'], movie_data['revenue'], movie_data['poster_path']))

        # Confirmar los cambios en la base de datos
        conn.commit()

        # Cerrar la conexión a la base de datos
        cursor.close()
        conn.close()

        self.stdout.write(self.style.SUCCESS('Successfully loaded the movie data'))

