from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        return super(Course, self).save(*args, *kwargs)

    def get_absolute_url(self):
        return reverse('course-list')

    @property
    def lessons(self):
        return self.lesson_set.all().order_by('position')

class Lesson(models.Model):
    title = models.CharField(max_length=120)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    position = models.IntegerField()
    thumbnail_image = models.ImageField(upload_to="media/")
    video_file_path = models.FileField(upload_to="media/")
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        return super(Lesson, self).save(*args, *kwargs)

    def get_absolute_url(self):
        return reverse('lesson-list')

class Video(models.Model):
    video_file_url = models.FileField(upload_to="media/")
    
    def __str__(self):
        return self.video_file_url