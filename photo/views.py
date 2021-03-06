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

def single_image(request,id):

    try:
        return Image.objects.get(pk=id)
    except Image.DoesNotExist:
        return False

    print(image_id)

    return render(request, "all-photos/single-photo.html",{"single":single,"Image":Image})

def search_place(request):

    if 'location' in request.GET and request.GET["location"]:
        search_place = request.GET.get("location")
        searched_places = Image.filter_by_location(search_place)
        message = f"{search_place}"

        return render(request,'all-photos/place.html',{"message":message, "location":searched_places})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-photos/place.html',{"message":message})
