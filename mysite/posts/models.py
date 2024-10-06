from django.db import models
from django.shortcuts import reverse
from students.models import Student


# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=20 , unique=True)
    body = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='posts/images/', null=True, blank=True)
    creator = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True,
                                related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.title}"


    @property
    def image_url(self):
        return f"/media/{self.image}"


    @property
    def show_url(self):
        url = reverse("posts.show", args =[self.id])
        return url

    @property
    def edit_url(self):
        url = reverse("posts.edit", args=[self.id])
        return url


    def get_absolute_url(self):
        url = reverse("posts.show", args=[self.id])
        return url
