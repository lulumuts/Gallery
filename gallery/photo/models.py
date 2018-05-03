from django.db import models

# Create your models here.


class Location(models.Model):
    place = models.CharField(max_length=60)

    def __str__(self):
        return self.place


    def save_location(self):
        return self.save()

class Category(models.Model):
    name= models.CharField(max_length=60)

    def __str__(self):
        return self.name

    def save_name(self):
        return self.save()

class Image(models.Model):
    image = models.ImageField(upload_to = 'photos/',blank=True)
    image_name = models.CharField(max_length=100)
    image_description = models.TextField()
    # image_location = models.ForeignKey(Location)
    # image_category = models.ForeignKey(Category)

    def __str__(self):
        return self.image


    def save_image(self):
        return self.save()

    @classmethod
    def update_image(cls,id,image,image_name,image_description):
        cls.objects.filter(id=id).update(image=image,image_name=image_name,image_description=image_description)
