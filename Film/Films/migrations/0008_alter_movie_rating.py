# Generated by Django 4.2.5 on 2024-01-29 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Films', '0007_rename_tittle_movie_title_director_info_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='rating',
            field=models.FloatField(),
        ),
    ]
