from django.urls import path
from newapp.apps import NewappConfig
from newapp.views import home
from . import views

# app_name = 'newapp'
app_name = NewappConfig.name

urlpatterns = [
    path('', views.home, name='home'),
    # path('', home, name='home')
]
