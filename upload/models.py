from django.db import models

# Create your models here.

class Upload(models.Model):
    upload_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to="media/")

    def __str__(self):
        return self.file



class UploadPrivate(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to="media/")
