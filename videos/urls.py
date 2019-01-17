from django.urls import path, include
from videos import views

app_name = "videos"

urlpatterns = [
    path('new/', views.VideoCreateView.as_view(), name="new"),
]
