from django.core.management.base import BaseCommand, CommandError
from movies.models import Genre, Movie, Person, Job, MovieCredit
from django.utils.timezone import timezone
from datetime import datetime

class Command(BaseCommand):
    help = "Loads movies and actors into the database"

    def handle(self, *args, **options):
        jobs = ['Director', 'Producer', 'Actor', 'Voice Actor']
        genres_data = ['Action', 'Adventure', 'Animation', 'Drama', 'Science Fiction', 'Thriller']

        # Crear géneros si no existen
        for name in genres_data:
            genre, created = Genre.objects.get_or_create(name=name)

        for job in jobs:
            j = Job(name=job)
            j.save()

        # Movie 1
        m1 = Movie(title='The Creator',
                   overview='Amid a future war between the human race and the forces of artificial intelligence, a hardened ex-special forces agent grieving the disappearance of his wife, is recruited to hunt down and kill the Creator, the elusive architect of advanced AI who has developed a mysterious weapon with the power to end the war—and mankind itself.',
                   release_date=datetime(2023, 9, 28, tzinfo=timezone.utc),
                   running_time=134,
                   budget=80_000_000,
                   tmdb_id=670292,
                   revenue=0,
                   poster_path='')

        # Asociar múltiples géneros a la película
        m1.save()
        m1.genres.add(Genre.objects.get(name='Action'))
        m1.genres.add(Genre.objects.get(name='Science Fiction'))  # Agregar más géneros si es necesario

        j = Job.objects.get(name='Actor')

        for name in ['John David Washington',
                     'Madeleine Yuna Voyles',
                     'Gemma Chan']:
            a = Person.objects.create(name=name)
            MovieCredit.objects.create(person=a, movie=m1, job=j)

        # Movie 2
        m2 = Movie(title='Otra Película',
                   overview='Descripción de Otra Película.',
                   release_date=datetime(20XX, XX, XX, tzinfo=timezone.utc),
                   running_time=XXX,
                   budget=XXXX,
                   tmdb_id=XXXXXX,
                   revenue=XXXXXX,
                   poster_path='')

        # Asociar múltiples géneros a la película
        m2.save()
        m2.genres.add(Genre.objects.get(name='Drama'))
        m2.genres.add(Genre.objects.get(name='Thriller'))  # Agregar más géneros si es necesario

        j = Job.objects.get(name='Actor')

        for name in ['Nombre Actor 1',
                     'Nombre Actor 2',
                     'Nombre Actor 3']:
            a = Person.objects.create(name=name)
            MovieCredit.objects.create(person=a, movie=m2, job=j)

        # Puedes continuar agregando más películas y actores de la misma manera
