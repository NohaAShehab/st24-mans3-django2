from django.db import models

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
