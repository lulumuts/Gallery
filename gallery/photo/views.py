from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt

# Create your views here.
def welcome(request):
    return render(request,'main.html')

def all_photos(request):
    date = dt.date.today()
    return render(request, 'all-photos/details.html', {"date" : date, })

def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_image = request.GET.get("category")
        searched_images = Image.search_image(category)
        message = f"{search_image}"

        return render(request, 'all-photos/search.html',{"message":message,"category": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-news/search.html',{"message":message})
