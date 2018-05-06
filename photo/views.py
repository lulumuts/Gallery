from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Image, Category, Location
import datetime as dt

# Create your views here.
def welcome(request):
    return render(request,'main.html')

def all_photos(request):
    collection = Image.all_photos
    return render(request,'all-photos/details.html', {"collection" : collection })

def search_photos(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_images = Image.search_image(search_term)
        message = f"{search_term}"

        return render(request,'all-photos/search.html',{"message":message, "category":searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-photos/search.html',{"message":message})

def single_image(request,image_id):

    image = Image.get_image_id

    return render(request, "all-photos/single-photo.html",{"image":image})
