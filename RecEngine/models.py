from django.db import models
from django.forms import ModelForm

class User(models.Model):
    name = models.CharField(max_length=50)
    number = models.IntegerField(default=0)
    email = models.EmailField()
    gender = models.CharField(max_length=5)
    password = models.CharField(max_length=10)
    dob = models.DateField()
    def __str__(self):
        return self.name




