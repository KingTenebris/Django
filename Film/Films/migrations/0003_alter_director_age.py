# Generated by Django 4.2.5 on 2024-01-22 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Films', '0002_director_age_director_info_movie_duration_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='director',
            name='age',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]