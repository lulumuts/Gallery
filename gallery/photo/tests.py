from django.test import TestCase
from .models import Image, Location,Category

# Create your tests here.
class ImageTestClass(TestCase):

    def setUp(self):
        self.image= Image(image_name='xmas', image_description = 'christmas in mallorca')

    def tearDown(self):
        Image.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))

    def test_save_method(self):
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_update_method(self):
        self.image.save_image()
        kwargs={'image':'/photo','image_name':'myname','image_description':'myself'}
        self.image.update_image(self.image.id,**kwargs)
        self.assertNotEqual("myname",self.image.image_name)




class CategoryTestClass(TestCase):

    def setUp(self):
        self.name= Category(name= 'holiday')

    def tearDown(self):
        Category.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.name,Category))

    def test_save_method(self):
        self.name.save_name()
        category = Category.objects.all()
        self.assertTrue(len(category) > 0)

class LocationTestClass(TestCase):

    def setUp(self):
        self.place= Location(place= 'mallorca')

    def tearDown(self):
        Location.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.place,Location))

    def test_save_method(self):
        self.place.save_location()
        location = Location.objects.all()
        self.assertTrue(len(location) > 0)
