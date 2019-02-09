from django.db import models
from django.urls import reverse


# Create your models here.

class VideoTutorial(models.Model):
    title = models.CharField(max_length=100)
    summary = models.TextField(max_length=500)
    thumbnail_image = models.ImageField(upload_to="media/")
    video_file = models.FileField(upload_to="media/")


    def get_absolute_url(self):
        return reverse("video_list")

    def __str__(self):
        return self.title
