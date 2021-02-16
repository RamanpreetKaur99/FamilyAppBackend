from __future__ import unicode_literals
from django.db import models
from core.models import MyUser, Family


class Groceries(models.Model):
    user = models.ForeignKey(MyUser, on_delete = models.CASCADE, null = True, blank=True) 
    family = models.ForeignKey(Family, on_delete = models.CASCADE, null = True, blank = True)
    item = models.CharField(max_length=100)
    purchased = models.BooleanField(default=False)

    def __str__(self):
        return self.item 

class ToDo(models.Model):
    user = models.ForeignKey(MyUser, on_delete = models.CASCADE, null = True, blank=True) 
    family = models.ForeignKey(Family, on_delete = models.CASCADE, null = True, blank = True)
    title = models.CharField(max_length=100)
    details = models.TextField(null = True, blank = True)
    deadline = models.DateField(null = True, blank = True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Event(models.Model):
    family = models.ForeignKey(Family, on_delete = models.CASCADE, null = True, blank = True) 
    title = models.CharField(max_length=500)
    allDay = models.BooleanField(default = True) 
    startDate = models.CharField(max_length=100)
    endDate = models.CharField(max_length=100)

    def __str__(self):
        return self.title 
        
class Bills(models.Model):
    electricity = models.CharField(max_length=25, default='1 0 0 0 0 0 0 0 0 0 0 0')
    water = models.CharField(max_length=25, default='0 0 0 0 0 0 0 0 0 0 0 0')
    watchman = models.CharField(max_length=25, default='0 0 0 0 0 0 0 0 0 0 0 0')
    maid = models.CharField(max_length=25, default='0 0 0 0 0 0 0 0 0 0 0 0')
    gascylinder = models.CharField(max_length=25, default='0 0 0 0 0 0 0 0 0 0 0 0')
    tv = models.CharField(max_length=25, default='0 0 0 0 0 0 0 0 0 0 0 0')
    family = models.ForeignKey(Family, on_delete = models.CASCADE, null = True, blank = True) 

    def __str__(self):
        return self.family.familyname 

        
    
