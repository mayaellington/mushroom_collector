from django.shortcuts import render, redirect

#import CreateView class
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.
from django.http import HttpResponse
from .models import Mushroom
from .forms import Shroom_HuntForm

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

def mushroom_detail(request, mushroom_id):
    mushroom = Mushroom.objects.get(id=mushroom_id)
    shroom_hunt_form = Shroom_HuntForm()
    return render(request, 'mushrooms/detail.html', {'mushroom': mushroom, 'shroom_hunt_form': shroom_hunt_form})

def add_shroom_hunt(request, mushroom_id):

    # create a ModelForm instance using data in request
    form = Shroom_HuntForm(request.POST)
    # validate
    if form.is_valid():
        # do some stuff
        #creates instance of feeding to be put in database
        #lets not save it yet, commit=False, bc we didnt add foreign key
        new_shroom_hunt = form.save(commit=False)
        new_shroom_hunt.mushroom_id = mushroom_id
        new_shroom_hunt.save() #adds feeding to database, asociated with same id as arg to function cat_id

    return redirect('detail', mushroom_id=mushroom_id)