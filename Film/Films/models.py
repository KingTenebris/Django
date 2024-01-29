from django.db import models

# Create your models here.
class Director(models.Model):
    name = models.CharField(max_length = 100)
    year = models.IntegerField()
    info = models.CharField(max_length = 500)


    # Att namn på director skrevs hans namn istället object1
    def __str__(self):
        return self.name

class Movie(models.Model):
    director = models.ForeignKey(Director, on_delete = models.CASCADE)
    title = models.CharField(max_length = 100) 
    year = models.IntegerField()
    rating = models.FloatField()
    genre = models.CharField(max_length = 100)

    # Att namn på filmen skrevs namn istället object1
    def __str__(self):
        return self.title