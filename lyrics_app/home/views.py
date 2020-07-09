from django.shortcuts import render
from . import google_login
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, "index.htm")

def album(request, id):
    albums = {1:'Rang De Basanti', 2:'Friends', 3:'Bahubali'}
    return render(request, "album.htm", {'albumName':albums[id]})

def song(request, id):
    songs = {1:'Namo Namo Hai Shankara', 2:'Kal Ho Na Ho', 3:'Hai Apna Dil To Aawara'}
    return render(request, "song.htm", {'songName':songs[id]})

def artist(request, id):
    artists = {1:'Arijit Singh', 2:'Shreya Ghoshal', 3:'Sonu Nigam'}
    return render(request, "artist.htm", {'artistName':artists[id]})

def login(request):
    print(request.data);
    google_login.validate(request);
    artists = {1:'Arijit Singh', 2:'Shreya Ghoshal', 3:'Sonu Nigam'}
    return render(request, "artist.htm", {'artistName':artists[id]})
