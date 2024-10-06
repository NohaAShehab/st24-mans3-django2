from django.shortcuts import render, redirect
from django.http import HttpResponse
from posts.forms import  PostForm
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView

from posts.models import Post


# Create your views here.


def create(request):
    form = PostForm() # model form

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES) # model form
        if form.is_valid():
            post = form.save()
            # return HttpResponse(f"valid, {post.id}")
            return redirect(post.show_url)



    return render(request, 'posts/create.html', {'form': form})

# class based views ??

# define views inside a class
# get all posts

class PostView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        return render(request, 'posts/index.html', {'posts': posts})



############# view as a class
## generic views --> prepare everything for you >??
class PostListView(ListView):
    model = Post
    template_name = 'posts/list.html'
    context_object_name = 'posts'



#### show ??
class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/show.html'
    context_object_name = 'post'



class PostUpdateView(UpdateView):
    form_class = PostForm
    template_name = 'posts/edit.html'
    model = Post



class PostCreateView(CreateView):
    form_class = PostForm
    template_name = 'posts/creategeneric.html'
    model = Post

    # redirect post absoulute url --> show


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/delete.html'
    success_url = '/posts/list'











