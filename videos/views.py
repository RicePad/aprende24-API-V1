from django.shortcuts import render
from django.views.generic import CreateView, ListView
from .models import VideoTutorial


class VideoListView(ListView):
    context_object_name = 'videos'
    model = VideoTutorial
    template_name = "video_list.html"

class VideoCreateView(CreateView):
    model = VideoTutorial
    fields = ("title", "summary", "thumbnail_image", "video_file")
    template_name = 'video_form.html'
