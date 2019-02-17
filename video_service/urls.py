"""video_dockerized URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import HomeView
from django.conf import settings
from django.conf.urls.static import static
from courses.views import CourseListView, LessonListView
from video_service.api import router
from video_service.views import list_all_cloudfare_data

urlpatterns = [
    path('', CourseListView.as_view(), name="lesson-list"),
    path('accounts/', include('allauth.urls')),
    path('api/v1/', include(router.urls)),
    path('api/auth', include('djoser.urls.authtoken')),
    path('courses/', CourseListView.as_view(), name="course-list"),
    path('lessons/', LessonListView.as_view(), name="lesson-list"),
    path('home/', HomeView.as_view(), name="home"),
    path('courses/', include('courses.urls', namespace='courses')),
    path('cloudflare', list_all_cloudfare_data, name="cloudflare"),
    path('admin/', admin.site.urls),
    

]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
