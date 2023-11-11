from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('about/', views.about, name='about'),
    path('get_objects_on_map/', views.get_objects_on_map, name='get_objects_on_map'),
]
