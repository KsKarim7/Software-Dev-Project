from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from musician.models import Musician

# Create your models here.

class Album(models.Model):
    RATING = (
        ("1","1"),
        ("2","2"),
        ("3","3"),
        ("4","4"),
        ("5","5"),
    )
    album_name = models.CharField(max_length=100)
    release_date = models.DateTimeField(default=timezone.now)
    # rating = models.FloatField(default=1, null=True, blank=True,validators=[MaxValueValidator(5), MinValueValidator(1)])  
    rating = models.CharField(choices=RATING, max_length=20, null=True, blank=True)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    


    def __str__(self):
        return f'{self.album_name} by {self.musician.first_name} {self.musician.last_name} 🎵'
