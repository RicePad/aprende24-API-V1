from django.urls import path, re_path
from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.CourseListView.as_view(), name="course-list"),
    path('update/<int:pk>/', views.CourseUpdateView.as_view(), name="course-update"),
    path('new/', views.CourseCreateView.as_view(), name="course-new"),
    path('cloudflare_videos', views.show_cloudflare_listview, name="lesson-videos"),
    re_path(r'^lesson/(?P<pk>\d+)$', views.LessonDetailView.as_view(), name="lesson-detail"),
    re_path(r'(?P<pk>\d+)$', views.CourseDetailView.as_view(), name="course-detail"),
    path('<slug>', views.CourseDetailView.as_view(), name="course-detail"),
    path('lessons/', views.LessonListView.as_view(), name="lesson-list"),
    path('lessons/upload_video', views.upload_video, name="video-upload"),
    path('lessons/new', views.LessonCreateView.as_view(), name="lesson-new"),
    path('lesson/<slug>', views.LessonDetailView.as_view(), name="lesson-detail"),
    path('lesson/<int:pk>/', views.LessonDetailView.as_view(), name="lesson-detail"),
]
