from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('album/<int:al_id>', views.album, name='Album'),
    path('song/<int:s_id>', views.song, name='Song'),
    path('artist/<int:ar_id>', views.artist, name='Artist'),
]