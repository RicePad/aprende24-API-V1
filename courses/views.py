from django.shortcuts import render
from django.views.generic import ListView, DetailView, View, CreateView
from .models import Course, Lesson

#USE FOR CLOUDFLARE API REQUESTS
import requests
import json
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import os

#ENV VARIABLES FOR CLOUDFLARE API
CLOUDFARE_USER = os.getenv("CLOUDFARE_USER")
CLOUDFARE_API = os.getenv("CLOUDFARE_API")
CLOUDFARE_ZONE_ID = os.getenv("CLOUDFARE_ZONE_ID")
CLOUDFARE_BASE_URL = os.getenv("CLOUDFARE_BASE_URL")

cloudflare_headers = { 'Content-Type': 'application/json',
                      'X-Auth-Key' : CLOUDFARE_API,
                      'X-Auth-Email': CLOUDFARE_USER ,}

# Create your views here.
class CourseCreateView(CreateView):
    model = Course
    fields = ("title", "description")
    template_name = "course_form.html"

class CourseListView(ListView):
    model = Course
    context_object_name = "course_list"
    template_name = "course_list.html"

class CourseDetailView(DetailView):
    model = Course
    context_object_name = "course_detail"
    template_name = "course_detail.html"

    def get_context_data(self, **kwargs):
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        context["lesson_list"] = Lesson.objects.all()
        context["course_list"] = Course.objects.all()
        return context

class LessonListView(ListView):
    model = Lesson
    context_object_name = "lesson_list"
    template_name = "lesson_list.html"

class LessonCreateView(CreateView):
    model = Lesson
    context_object_name = "lesson_detail"
    fields = (  "title",
                "course",
                "position",
                "video_url",
                "thumbnail_image",
                "video_file"
                )
    template_name = "lesson_form.html"

class LessonDetailView(DetailView):
    model = Lesson
    context_object_name = "lesson_detail"
    template_name = "lesson_detail.html"

    def get_context_data(self, **kwargs):
        context = super(LessonDetailView, self).get_context_data(**kwargs)
        context["lesson_list"] = Lesson.objects.all()
        context["course_list"] = Course.objects.all()
        return context


def fetch_cloudflareAPI_video_list():
    api_url = "{0}zones/{1}/media".format(CLOUDFARE_BASE_URL, CLOUDFARE_ZONE_ID)
    response = requests.get(api_url, headers=cloudflare_headers)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

def show_cloudflare_listview(request):
    lesson = Lesson.objects.all
    cloudflare_list = fetch_cloudflareAPI_video_list()
    return render(request, "cloudflare_list_videos.html", {"cloudflare_list_videos": cloudflare_list['result'], "lesson_list": lesson})
