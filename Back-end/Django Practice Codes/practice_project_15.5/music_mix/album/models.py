from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from musician.models import Musician

# Create your models here.

class Album(models.Model):
    album_name = models.CharField(max_length=100)
    date_time_field = models.DateTimeField(default=timezone.now)
    rating = models.FloatField(default=1, null=True, blank=True,validators=[MaxValueValidator(5), MinValueValidator(1)])  
    author = models.ForeignKey(Musician, on_delete=models.CASCADE)
    


    def __str__(self):
        return f'{self.album_name} by {self.author.first_name} {self.author.last_name} 🎵'
