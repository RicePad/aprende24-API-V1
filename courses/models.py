from django.db import models
from django.urls import reverse
from video_service.storange_backends import PublicMediaStorage, PrivateMediaStorage
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
    video_url = models.CharField(max_length=200)
    thumbnail_image = models.ImageField(storage=PublicMediaStorage())
    video_file = models.FileField(storage=PublicMediaStorage(), null=True, verbose_name="")
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        return super(Lesson, self).save(*args, *kwargs)

    def get_absolute_url(self):
        return reverse('lesson-list')
