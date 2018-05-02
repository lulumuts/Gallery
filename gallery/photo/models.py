from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to = 'photos/',blank=True)
    image_name = models.CharField(max_length=100)
    image_description = models.TextField()

    def __str__(self):
        return self.image


class Location(models.Model):
    place = models.CharField(max_length=60)

    def __str__(self):
        return self.place

class Category(models.Model):
    name= models.CharField(max_length=60)

    def __str__(self):
        return self.name
