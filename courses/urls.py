from django.urls import path, re_path
from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.CourseListView.as_view(), name="course-list"),
    path('new/', views.CourseCreateView.as_view(), name="course-new"),
    re_path(r'(?P<pk>\d+)$', views.CourseDetailView.as_view(), name="course-detail"),
    path('<slug>', views.CourseDetailView.as_view(), name="course-detail"),
    path('lessons/', views.LessonListView.as_view(), name="lesson-list"),
]
