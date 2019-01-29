from django.db import models

# Create your models here.
from video_service.storange_backends import PublicMediaStorage, PrivateMediaStorage

class Upload(models.Model):
    upload_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(storage=PublicMediaStorage())

    def __str__(self):
        return self.file



class UploadPrivate(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(storage=PrivateMediaStorage())
