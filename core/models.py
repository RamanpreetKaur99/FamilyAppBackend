from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser

class Family(models.Model):
    familyname = models.CharField(max_length = 100)

    def __self__(str):
        return self.familyname 

class MyUser(AbstractUser):
    name = models.CharField(max_length=100,null = True, blank = True)
    family = models.ForeignKey(Family, on_delete = models.SET_NULL,null = True, blank=True)