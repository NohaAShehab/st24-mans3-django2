from django.db import models
from django.shortcuts import reverse
# Create your models here.

class Track(models.Model):
    name = models.CharField(max_length=100, unique=True)
    capacity = models.IntegerField(default=0, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


    def __str__(self):
        return f'{self.name}'


    @property
    def show_url(self):
        url = reverse('tracks.show', args=[self.id])
        return url
