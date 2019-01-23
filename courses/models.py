from django.db import models
from django.urls import reverse
from video_service.storange_backends import PublicMediaStorage, PrivateMediaStorage

# Create your models here.
class Course(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=120)
    description = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('course_list')


class Lesson(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=120)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    position = models.IntegerField()
    video_url = models.CharField(max_length=200)
    thumbnail_image = models.ImageField(storage=PublicMediaStorage())


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('course_list')
