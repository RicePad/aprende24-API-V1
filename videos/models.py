from django.db import models

# Create your models here.

class VideoTutorials(models.Model):
    title = models.CharField(max_length=100)
    summary = models.TextField(max_length=500)
    thumbnail_image = models.ImageField(upload_to="thumbnail_images/")


    def __str__(self):
        return self.title
