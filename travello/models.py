from django.db import models

# Create your models here.

# Tạo class Destination để quản lý các tour
#  Models các tour

class Destination(models.Model):
    
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)