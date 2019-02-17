from django.shortcuts import render
from django.views.generic import ListView, DetailView, View, CreateView, UpdateView
from .models import Course, Lesson, Video
from django.contrib.auth.mixins import LoginRequiredMixin


#USE FOR CLOUDFLARE API REQUESTS
import requests
import json
import os
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from courses.forms import VideoUploadForm
from tusclient import client

#ENV VARIABLES FOR CLOUDFLARE API
CLOUDFARE_USER = os.getenv("CLOUDFARE_USER")
CLOUDFARE_API = os.getenv("CLOUDFARE_API")
CLOUDFARE_ZONE_ID = os.getenv("CLOUDFARE_ZONE_ID")
CLOUDFARE_BASE_URL = os.getenv("CLOUDFARE_BASE_URL")

cloudflare_headers = { 'Content-Type': 'application/json',
                      'X-Auth-Key' : CLOUDFARE_API,
                      'X-Auth-Email': CLOUDFARE_USER ,}

# Create your views here.
class CourseCreateView(LoginRequiredMixin,CreateView):
    model = Course
    fields = ("title", "description")
    template_name = "course_form.html"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

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

class CourseUpdateView(LoginRequiredMixin,UpdateView):
    model = Course
    fields = ['title', 'description']
    template_name = "course_edit_form.html"


class LessonListView(ListView):
    model = Lesson
    context_object_name = "lesson_list"
    template_name = "lesson_list.html"

class LessonCreateView(LoginRequiredMixin,CreateView):
    model = Lesson
    context_object_name = "lesson_detail"
    fields = (  "title",
                "course",
                "position",
                "thumbnail_image",
                "video_file_path"
                )
    template_name = "lesson_form.html"
    success_url = "/lessons/"

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        # create a form instance and populate it with data from the request:        
        video_file_url = form.cleaned_data.get('video_file_path')    
        TUS_ENDPOINT = "https://api.cloudflare.com/client/v4/zones/{0}/media".format(CLOUDFARE_ZONE_ID)
        HEADERS = {'X-Auth-Key': CLOUDFARE_API,
                    'X-Auth-Email': CLOUDFARE_USER}

        CHUNK_SIZE = 5242880
        
        my_client = client.TusClient(TUS_ENDPOINT, headers=HEADERS)
        uploader = my_client.uploader(file_stream=video_file_url, chunk_size=CHUNK_SIZE)
        uploader.upload()

        # redirect to a new URL:
        return super().form_valid(form)

class LessonDetailView(DetailView):
    model = Lesson
    context_object_name = "lesson_detail"
    template_name = "lesson_detail.html"

    def get_context_data(self, **kwargs):
        context = super(LessonDetailView, self).get_context_data(**kwargs)
        context["lesson_list"] = Lesson.objects.all()
        context["course_list"] = Course.objects.all()
        return context

class LessonUpdateView(LoginRequiredMixin,UpdateView):
    model = Lesson
    fields = ['title', 'position', 'thumbnail_image', 'video_file_path',]
    template_name = "lesson_edit_form.html"
    success_url = "/lessons/"

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        # create a form instance and populate it with data from the request:        
        video_file_url = form.cleaned_data.get('video_file_path')    
        TUS_ENDPOINT = "https://api.cloudflare.com/client/v4/zones/{0}/media".format(CLOUDFARE_ZONE_ID)
        HEADERS = {'X-Auth-Key': CLOUDFARE_API,
                    'X-Auth-Email': CLOUDFARE_USER}

        CHUNK_SIZE = 5242880
        
        my_client = client.TusClient(TUS_ENDPOINT, headers=HEADERS)
        uploader = my_client.uploader(file_stream=video_file_url, chunk_size=CHUNK_SIZE)
        uploader.upload()

        # redirect to a new URL:
        return super().form_valid(form)



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

def upload_video(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = VideoUploadForm(request.POST, request.FILES)
        video_file_url = request.FILES['video_file_url']

        # check whether form it's valid:
        if form.is_valid():
            form.save()

            TUS_ENDPOINT = "https://api.cloudflare.com/client/v4/zones/{0}/media".format(CLOUDFARE_ZONE_ID)
            HEADERS = {'X-Auth-Key': CLOUDFARE_API,
                       'X-Auth-Email': CLOUDFARE_USER}

            CHUNK_SIZE = 5242880
            
            my_client = client.TusClient(TUS_ENDPOINT, headers=HEADERS)

            uploader = my_client.uploader(file_stream=video_file_url, chunk_size=CHUNK_SIZE)

            uploader.upload()

            # redirect to a new URL:
            return HttpResponseRedirect('/lessons/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = VideoUploadForm()

    return render(request, 'upload_video_form.html', {'form': form})
