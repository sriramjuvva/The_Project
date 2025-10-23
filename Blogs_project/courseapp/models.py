from django.db import models
from django.http import JsonResponse,HttpResponse
from ckeditor.fields import RichTextField

# Create your models here.


class Courses_Model(models.Model):
    Course_name = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.Course_name

class Lesson(models.Model):
    course = models.ForeignKey(Courses_Model, on_delete=models.CASCADE, related_name="lessons")
    day_number = models.PositiveIntegerField(unique= True)
    title = models.CharField(max_length=100)
    content = RichTextField()

    



