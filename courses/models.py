from django.db import models
from django.urls import reverse

# Create your models here.
class Course(models.Model):
    slug = models.SlugField()
    course_title = models.CharField(max_length=120)
    course_description = models.TextField()

    def __str__(self):
        return self.course_title

    def get_absolute_url(self):
        return reverse('video_list')


class Lesson(models.Model):
    slug = models.SlugField()
    lesson_title = models.CharField(max_length=120)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    position = models.IntegerField()
    video_url = models.CharField(max_length=200)
    thumbnail_image = models.ImageField()


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')
