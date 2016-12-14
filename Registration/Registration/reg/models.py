from __future__ import unicode_literals

from django.db import models

# Create your models here.



class Registern(models.Model):

   Name = models.CharField(max_length=400)
   Username = models.CharField(max_length=400)
   Password = models.CharField(max_length=400)
   CPassword = models.CharField(max_length=400)
   
   def __str__(self):
      return ' '.join([
        self. ordering,

    ])
      
class car_info(models.Model):

   location = models.CharField(max_length=400)
   from_id = models.CharField(max_length=400)
   to = models.CharField(max_length=400)
   
   def __str__(self):
      return ' '.join([
        self. ordering,

    ])