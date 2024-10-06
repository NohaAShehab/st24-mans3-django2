from django.urls import path
from tracks.views import  index, create, show

urlpatterns = [
    path("", index, name="tracks.index"),
    path('create', create, name="tracks.create"),
    path("<int:id>", show, name="tracks.show"),
]
