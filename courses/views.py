from django.shortcuts import render
from django.views.generic import ListView, DetailView, View, CreateView
from .models import Course, Lesson
# Create your views here.


class CourseListView(ListView):
    model = Course
    context_object_name = 'course_list'
    template_name = 'course_list.html'


class CourseCreateView(CreateView):
    model = Course
    fields = ("slug", "title", "description")
    template_name = 'course_form.html'
