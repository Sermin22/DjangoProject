from django.urls import path
from dogs.apps import DogsConfig
from dogs.views import dogs_list
from . import views

# app_name = 'dogs'
app_name = DogsConfig.name

urlpatterns = [
    path('base/', views.base, name='base'),
    path('dogs_list/', views.dogs_list, name='dogs_list'),
    path('dogs_detail/<int:pk>/', views.dogs_detail, name='dogs_detail'),
    # path('', name_models, name='name_models')
]
