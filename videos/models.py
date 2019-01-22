from django.db import models
from django.urls import reverse
from video_dockerized.storange_backends import PublicMediaStorage, PrivateMediaStorage


# Create your models here.

class VideoTutorial(models.Model):
    title = models.CharField(max_length=100)
    summary = models.TextField(max_length=500)
    thumbnail_image = models.ImageField(storage=PublicMediaStorage())
    video_file = models.FileField(storage=PublicMediaStorage(), null=True, verbose_name="")


    def get_absolute_url(self):
        return reverse("video_list")

    def __str__(self):
        return self.title
