from django.contrib import admin
from .models import Course, Lesson, Video

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    pass

admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Video)
