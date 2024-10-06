from django.shortcuts import render, reverse, redirect
from tracks.models import Track
from tracks.forms import TrackForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import  login_required
# Create your views here.


def index(request):
    tracks = Track.objects.all()
    return render(request, 'tracks/index.html', {'tracks': tracks})



@login_required()
def create(request):
    form = TrackForm()
    if request.method == 'POST':
        form = TrackForm(request.POST)
        if form.is_valid():
            track = Track(name=form.cleaned_data['name'],capacity=form.cleaned_data['capacity'],
                          owner=request.user)
            track.save()
            url = reverse('tracks.index')
            return redirect(url)

    return render(request, 'tracks/create.html', {'form': form})



def show(request, id):
    track = get_object_or_404(Track, pk=id)
    return render(request, 'tracks/show.html', {'track': track})