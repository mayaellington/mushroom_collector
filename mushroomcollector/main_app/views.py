from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Mushroom

def home(request):
    return HttpResponse('<h1>Mushroom Collector Home Page</h1>')

def about(request):
    return render(request, 'about.html')

def mushrooms_index(request):
    mushrooms = Mushroom.objects.all()
    return render(request, 'mushrooms/index.html', {'mushrooms': mushrooms}) 

def mushroom_detail(request, shroom_id):
    mushroom = Mushroom.objects.get(id=shroom_id)
    return render(request, 'mushrooms/detail.html', {'mushroom': mushroom})