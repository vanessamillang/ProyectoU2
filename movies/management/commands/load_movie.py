import os
import environ
import requests
import psycopg2

env = environ.Env()
environ.Env.read_env('.env')
print('API_KEY: ', env('API_KEY'))
print('API_TOKEN: ', env('API_TOKEN'))

'''
url --request GET \
     --url 'https://api.themoviedb.org/3/movie/76341?language=en-US' \
     --header 'Authorization: Aasdfqwer' \
     --header 'accept: application/json'
'''
headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {env('API_TOKEN')}"
}

movie_id = 76341
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
    host="pwalejandro.ddns.net",
    port="8080"
)
cursor = conn.cursor()

# Insertar información de la película en la base de datos
insert_movie_query = "INSERT INTO movies_movie (movie_id, title, overview, release_date) VALUES (%s, %s, %s, %s)"
cursor.execute(insert_movie_query, (movie_data['id'], movie_data['title'], movie_data['overview'], movie_data['release_date']))

# Insertar información del elenco en la base de datos
for actor in credits['cast'][:10]:
    insert_cast_query = "INSERT INTO cast (actor_id, name, movie_id) VALUES (%s, %s, %s)"
    cursor.execute(insert_cast_query, (actor['id'], actor['name'], movie_data['id']))

# Insertar información del equipo en la base de datos
for job in credits['crew'][:15]:
    insert_crew_query = "INSERT INTO crew (name, department, job, movie_id) VALUES (%s, %s, %s, %s)"
    cursor.execute(insert_crew_query, (job['name'], job['department'], job['job'], movie_data['id']))

# Confirmar los cambios en la base de datos
conn.commit()

# Cerrar la conexión a la base de datos
cursor.close()
conn.close()




