from rest_framework.routers import DefaultRouter
from courses import api_views as myapp_views

router = DefaultRouter()
router.register(r'courses', myapp_views.CourseAPIViewSet)
router.register(r'lessons', myapp_views.LessonAPIViewSet)
