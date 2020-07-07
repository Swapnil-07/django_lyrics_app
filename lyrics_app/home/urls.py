from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('album/<int:id>', views.album, name='Album'),
    path('song/<int:id>', views.song, name='Song'),
    path('artist/<int:id>', views.artist, name='Artist'),
]