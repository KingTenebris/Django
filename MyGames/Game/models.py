from django.db import models

# Create your models here.

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