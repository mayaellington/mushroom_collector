from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('mushrooms/', views.mushrooms_index, name='index'),
    path('mushrooms/<int:shroom_id>', views.mushroom_detail, name='detail'),
    path('mushrooms/create/', views.MushroomCreate.as_view(), name='mushrooms_create'),
    path('mushrooms/<int:pk>/update/', views.MushroomUpdate.as_view(), name='mushrooms_update'),
    path('mushrooms/<int:pk>/delete/', views.MushroomDelete.as_view(), name='mushrooms_delete'),

]