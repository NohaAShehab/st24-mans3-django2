
from django.urls import path
from students.views import hello, liststds, profile
urlpatterns = [
    path("hello", hello, name="students.hello"),
    path("list", liststds, name="students.list"),
    path("profile/<int:id>", profile, name="students.profile"),
]
