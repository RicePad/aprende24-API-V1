from django import forms
from courses.models import Video


class VideoUploadForm(forms.ModelForm):
     class Meta:
        fields = ('video_file_url',)
        model = Video
