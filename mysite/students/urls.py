
from django.urls import path
from students.views import hello, liststds, profile, index, show, delete
urlpatterns = [
    path("hello", hello, name="students.hello"),
    path("list", liststds, name="students.list"),
    path("profile/<int:id>", profile, name="students.profile"),
    path('',index, name='students.index'),
    path("<int:id>", show, name="students.show"),
    path("delete/<int:id>", delete, name="students.delete"),
]
