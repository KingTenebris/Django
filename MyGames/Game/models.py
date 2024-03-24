from django.db import models

# Create your models here.
#! DO not touch this
class Phase(models.Model):

    state = models.CharField(max_length = 100)

    def __str__(self):
        return self.state
        
class Developer(models.Model):

    name = models.CharField(max_length = 100)
    year = models.IntegerField(null = True, blank = True)
    info = models.TextField(null = True, blank = True)

    def __str__(self):
        return self.name

class Platform(models.Model):

    name = models.CharField(max_length = 100)
    year = models.IntegerField(null = True, blank = True)
    info = models.TextField(null = True, blank = True)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    genre = models.CharField(max_length = 100)

    def __str__(self):
        return self.genre
    
class Game(models.Model):
    name = models.CharField(max_length = 100)
    year = models.IntegerField()
    phase = models.ForeignKey(Phase, on_delete = models.CASCADE)
    developer = models.ForeignKey(Developer, on_delete = models.CASCADE)
    platform = models.ForeignKey(Platform, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)

    def __str__(self):
        return self.name