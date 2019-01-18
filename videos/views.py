from django.shortcuts import render
from django.views.generic import CreateView
from .models import VideoTutorial


class VideoCreateView(CreateView):
    model = VideoTutorial
    fields = ("title", "summary", "thumbnail_image", "video_file")
    template_name = 'video_form.html'
