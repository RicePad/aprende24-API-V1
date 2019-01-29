from django.contrib import admin
from .models import Course, Lesson

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    pass

admin.site.register(Course)
admin.site.register(Lesson)
