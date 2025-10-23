from django.contrib import admin
from .models import * 


# Register your models here.
@admin.register(Courses_Model)
@admin.register(Lesson)

class Courses_ModelAdmin(admin.ModelAdmin):
    pass
class LessonAdmin(admin.ModelAdmin):
    pass

