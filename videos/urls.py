from django.urls import path, include
from videos import views

app_name = "videos"

urlpatterns = [
    path('', views.VideoListView.as_view(), name="video_list"),
    path('new/', views.VideoCreateView.as_view(), name="new"),


]
