from django.shortcuts import render
from django.views.generic import ListView, DetailView, View, CreateView
from .models import Course, Lesson

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

class LessonListView(ListView):
    model = Lesson
    context_object_name = "lesson_list"
    template_name = "lesson_list.html"
