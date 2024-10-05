from django.db import models
from django.shortcuts import  reverse
from tracks.models import Track

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, null=True, unique=True)
    grade =models.IntegerField(default=0, null=True)
    # image = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='students/images', null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    track = models.ForeignKey(Track, on_delete=models.SET_NULL,
                              related_name='students',
                              null=True)
    # student models needs object --> so it can deal with

    ####
    def __str__(self):
        return f'{self.name}'

    @property
    def show_url(self):
        # self.id
        url = reverse('students.show', args=[self.id])
        return url

    @property
    def delete_url(self):
        # self.id
        url = reverse('students.delete', args=[self.id])
        return url


    @property
    def image_url(self):
        return f'/media/{self.image}'

