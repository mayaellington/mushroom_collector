from django.forms import ModelForm
from .models import Shroom_Hunt

class Shroom_HuntForm(ModelForm):
  class Meta:
    model = Shroom_Hunt
    fields = ['date', 'location', 'recent_rain']