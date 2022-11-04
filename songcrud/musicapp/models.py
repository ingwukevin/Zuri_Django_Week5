from django.db import models
from datetime import datetime

# Create your models here.

class Artiste(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    age= models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Song(models.Model):
    title= models.CharField(max_length=50)
    date_released=models.DateField(default=datetime.today)
    likes=models.PositiveIntegerField()
    artiste_id=models.ForeignKey("Artiste", on_delete=models.CASCADE)

    def __str__(self):
        return(f"{self.title}")

class Lyrics(models.Model):
    content=models.CharField(max_length=5000)
    song_id=models.ForeignKey("Song", on_delete=models.CASCADE)
