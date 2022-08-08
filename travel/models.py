from django.db import models
# Create your models here.
class destination(models.Model):
    name = models.CharField(max_length=100) #for loop
    desc = models.TextField()
    img = models.ImageField(upload_to='img')
    offer = models.BooleanField(default=False) #if loop
    price = models.IntegerField()