from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "index.htm")

def album(request, al_id):
    albums = {1:'Rang De Basanti', 2:'Friends', 3:'Bahubali'}
    return render(request, "album.htm", {'albumName':albums[al_id]})

def song(request, s_id):
    songs = {1:'Namo Namo Hai Shankara', 2:'Kal Ho Na Ho', 3:'Hai Apna Dil To Aawara'}
    return render(request, "song.htm", {'songName':songs[s_id]})

def artist(request, ar_id):
    artists = {1:'Arijit Singh', 2:'Shreya Ghoshal', 3:'Sonu Nigam'}
    return render(request, "artist.htm", {'artistName':artists[ar_id]})

