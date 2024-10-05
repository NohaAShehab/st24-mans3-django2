from django.db import models
from django.shortcuts import  reverse

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, null=True, unique=True)
    grade =models.IntegerField(default=0, null=True)
    image = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

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

