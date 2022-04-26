from django.shortcuts import render

#import CreateView class
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.
from django.http import HttpResponse
from .models import Mushroom

class MushroomCreate(CreateView):
    model = Mushroom
    fields = '__all__' #this is two underscores
class MushroomUpdate(UpdateView):
    model = Mushroom
    fields = ['name', 'scientific_name', 'description', 'season', 'edibility']

class MushroomDelete(DeleteView):
    model = Mushroom
    success_url = '/mushrooms/' 

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