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
    image_location = models.ForeignKey(Location)
    image_category = models.ForeignKey(Category)

    def __str__(self):
        return self.image_name

    def save_image(self):
        return self.save()

    @staticmethod
    def update_image(id,image,image_name,image_description):

        Image.objects.filter(pk=id).update(image=image,image_name=image_name,image_description=image_description)

    def get_image_id(self,id):
        return self.objects.get(pk=id)

    @classmethod
    def search_image(cls,search_term):
        image = cls.objects.filter(image_category__name__icontains=search_term)
        print(image)
        return image