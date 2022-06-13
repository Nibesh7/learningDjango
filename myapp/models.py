from distutils.command.upload import upload
from email.mime import image
from email.policy import default
from django.db import models

class Product(models.Model):
    def  __str__(self):
        return self.name #display name instead of object in admin panel
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    desc= models.CharField(max_length=200)
    image=models.ImageField(blank=True,upload_to='images')
