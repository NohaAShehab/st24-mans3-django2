from django.shortcuts import render
from django.http import HttpResponse
from posts.forms import  PostForm
# Create your views here.


def create(request):
    form = PostForm() # model form

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES) # model form
        if form.is_valid():
            post = form.save()
            return HttpResponse(f"valid, {post.id}")



    return render(request, 'posts/create.html', {'form': form})