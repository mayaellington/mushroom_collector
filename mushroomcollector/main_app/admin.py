from django.contrib import admin

# Register your models here.
from .models import Mushroom, Park, Shroom_Hunt

admin.site.register(Mushroom)
admin.site.register(Shroom_Hunt)
admin.site.register(Park)