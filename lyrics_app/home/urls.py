from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('album/<int:id>', views.album, name='Album'),
    path('song/<int:id>', views.song, name='Song'),
    path('artist/<int:id>', views.artist, name='Artist'),
    path('login', views.login, name='Login'),
    path('post-album', views.postAlbum, name='post_album'),
    path('create-user', views.createUser, name='create_user'),
]