from django.urls import path
from posts.views import (create, PostView, PostListView, PostDetailView,
                         PostUpdateView, PostCreateView, PostDeleteView)
urlpatterns = [
    path('create', create, name='posts.create'),
    path("", PostView.as_view(), name='posts.index'),
    path('list', PostListView.as_view(), name='posts.list'),
    path("<int:pk>", PostDetailView.as_view(), name='posts.show'),
    path("<int:pk>/edit", PostUpdateView.as_view(), name='posts.edit'),
    path("forms/create", PostCreateView.as_view(), name='posts.forms.create'),
    path("<int:pk>/delete", PostDeleteView.as_view(), name='posts.delete'),

]