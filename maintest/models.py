
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    class_choice = models.IntegerField()
    accuracy = models.FloatField(default=0.0)
    wpm = models.FloatField(default=0.0)
    cpm = models.FloatField(default=0.0)