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
                )
    template_name = "lesson_form.html"

class LessonDetailView(DetailView):
    model = Lesson
    context_object_name = "lesson_detail"
    template_name = "lesson_detail.html"
