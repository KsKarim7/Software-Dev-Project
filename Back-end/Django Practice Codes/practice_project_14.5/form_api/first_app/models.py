from django.db import models

# Create your models here.

class StudentModel(models.Model):
    roll = models.PositiveBigIntegerField()
    serial_no =  models.BigAutoField(primary_key=True,default=0)
    name = models.CharField(max_length=20)
    profile_pic = models.ImageField(default=None, blank=True)
    email = models.EmailField(default="xxx@xxx.com")
    father_name = models.CharField(max_length=30)
    address = models.TextField()
    session_fee = models.BooleanField(default=False)
    payment_date = models.DateField(default=None)
