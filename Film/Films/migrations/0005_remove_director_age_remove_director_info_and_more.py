# Generated by Django 4.2.5 on 2024-01-22 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Films', '0004_alter_movie_duration_alter_movie_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='director',
            name='age',
        ),
        migrations.RemoveField(
            model_name='director',
            name='info',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='genre',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='year',
        ),
    ]