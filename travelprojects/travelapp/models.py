from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='pics')
    description = models.TextField()

    def __str__ (self):
        return self.name

class photos(models.Model):
    names=models.CharField(max_length=250)
    images = models.ImageField(upload_to='pics')
    descri = models.TextField()

    def __str__ (self):
        return self.names

