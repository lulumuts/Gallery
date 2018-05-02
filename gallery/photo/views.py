from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt

# Create your views here.
def welcome(request):
    return render(request,'main.html')

def all_photos(request):
    date = dt.date.today()
    return render(request, 'all-photos/details.html', {"date" : date, })
