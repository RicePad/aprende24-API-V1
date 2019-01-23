from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.CourseListView.as_view(), name="course-list"),
    path('new/', views.CourseCreateView.as_view(), name="course-new"),
    path('<slug>', views.CourseDetailView.as_view(), name="course-detail"),
]
