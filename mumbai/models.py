from django.db import models
from django.conf import settings

class PassengerDetails(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    date = models.DateTimeField()