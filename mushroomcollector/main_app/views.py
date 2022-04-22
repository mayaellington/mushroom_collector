from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

class Mushroom:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, scientific_name, description, season, edibility):
    self.name = name
    self.scientific_name = scientific_name
    self.description = description
    self.season = season
    self.edibility = edibility

mushrooms = [
  Mushroom('Fly Agaric', 'Amanita muscaria', 'Cap yellow to orange with white scales that are remnants of the universal veil', 'Summer/Fall', 'Poisonous'),
  Mushroom('Morel', 'Morchella esculenta', 'Cap resembles an inverted pine cone with ridges and deep pits', 'Spring', 'Very'),
  Mushroom('Maze Bracket', 'Daedalea quercina', 'Gray to light brown, leathery, shelf with mazelike lower surface', 'Spring/Fall', 'Inedible'),
]

def home(request):
    return HttpResponse('<h1>hiii</h1>')

def about(request):
    return render(request, 'about.html')

def mushrooms_index(request):
    return render(request, 'mushrooms/index.html', {'mushrooms': mushrooms})