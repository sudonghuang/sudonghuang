from django.db import models


# Create your models here.

class Book(models.Model):
    filename = models.CharField(max_length=100)
    file = models.FileField(upload_to='E:\\myfile')



class Image(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')