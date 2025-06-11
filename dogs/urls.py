from django.urls import path
from django.views.decorators.cache import cache_page
from dogs.apps import DogsConfig
from dogs import views
from dogs.views import DogListView, DogDetailView, DogCreateView, DogUpdateView, DogDeleteView

# app_name = 'dogs'
app_name = DogsConfig.name

urlpatterns = [
    path('base/', views.base, name='base'),
    path('dog_list/', DogListView.as_view(), name='dog_list'),
    path('dog/<int:pk>/', cache_page(60)(DogDetailView.as_view()), name='dog_detail'),
    path('dog/create/', DogCreateView.as_view(), name='dog_create'),
    path('dog/<int:pk>/update/', DogUpdateView.as_view(), name='dog_update'),
    path('dog/<int:pk>/delete/', DogDeleteView.as_view(), name='dog_delete'),
    # path('dogs_list/', views.dogs_list, name='dogs_list'),
    # path('dogs_detail/<int:pk>/', views.dogs_detail, name='dogs_detail'),
]
