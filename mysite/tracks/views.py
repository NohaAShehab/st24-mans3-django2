from django.shortcuts import render
from tracks.models import Track

# Create your views here.


def index(request):
    tracks = Track.objects.all()
    return render(request, 'tracks/index.html', {'tracks': tracks})