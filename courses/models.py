from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Course(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=120)
    description = models.TextField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = slugify(self.title)
            while True:
                try:
                    course = Course.objects.get(slug=slug)
                    if course == self:
                        self.slug = slug
                        break
                    else:
                        slug = slug + '-'
                except:
                    self.slug = slug
                    break
        return super(Course, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('course-list')

    @property
    def lessons(self):
        return self.lesson_set.all().order_by('position')

class Lesson(models.Model):
    title = models.CharField(max_length=120)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    position = models.IntegerField()
    thumbnail_image = models.ImageField(upload_to="thumbnail_images/")
    video_file_path = models.FileField(upload_to="video_files/", validators=[FileExtensionValidator(allowed_extensions=['mp4','mkv','mov', 'avi', 'flv', 'mpg','wmv'])])
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = slugify(self.title)
            while True:
                try:
                    lesson = Lesson.objects.get(slug=slug)
                    if lesson == self:
                        self.slug = slug
                        break
                    else:
                        slug = slug + '-'
                except:
                    self.slug = slug
                    break
        return super(Lesson, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('lesson-list')

class Video(models.Model):
    video_file_url = models.FileField(upload_to="media/")
    
    def __str__(self):
        return self.video_file_url