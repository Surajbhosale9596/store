from cgi import FieldStorage
from operator import mod
from django.db import models

# Create your models here.
class Item(models.Model):
    name=models.CharField(max_length=255)
    price=models.FloatField()
    img=models.CharField(max_length=2500)




                

    

