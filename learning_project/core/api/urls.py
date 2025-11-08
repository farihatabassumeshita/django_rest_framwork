from home.views import index, person_list
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('index/', index),
    path('person/', person_list)
]
