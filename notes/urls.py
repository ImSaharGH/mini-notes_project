from django.urls import path 
from . import views

urlpatterns = [
    path('' , views.Notes_list_view , name='Notes_list'),
]