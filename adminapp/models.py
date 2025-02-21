from django.db import models

# Create your models here.
class BRANCHES(models.Model):
    Name=models.CharField(max_length=23)
    Image=models.ImageField(upload_to='image',default='null.jpeg')
class SALOON(models.Model):
    Sname=models.CharField(max_length=23)
    Branch=models.CharField(max_length=22)
    Description=models.CharField(max_length=100)
    Emage=models.ImageField(upload_to='emage',default='null.jpeg')
class SERVICES(models.Model):
    Serv=models.CharField(max_length=50)
    Salon=models.CharField(max_length=70)
    Price=models.IntegerField()
    Description=models.CharField(max_length=200)
    IImage=models.ImageField(upload_to='iimage',default='null.jpeg')