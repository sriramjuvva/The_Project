from django.shortcuts import render
from django.http import JsonResponse,HttpResponse,FileResponse
from .models import *
from . import serializers 
from . serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required



# Create your views here.

@api_view(['GET'])
def Courses_to_show(request):
    all_courses = Courses_Model.objects.all().order_by('id')  # simpler than raw()
    serializer = courseserializer(all_courses, many=True)
    context = {'courses': serializer.data}
    return render(request, 'base.html', context)



@api_view(['GET'])
def fetching_the_content(request,course_name):
    getting_id_from_courses_model = Courses_Model.objects.get(Course_name = course_name)
    id_of_course = getting_id_from_courses_model.id
    showing_titles_of_days = Lesson.objects.get(course=id_of_course)
    return HttpResponse(str(showing_titles_of_days.day_number)+"-"+showing_titles_of_days.title)

@login_required(login_url='')
def fetching_the_content(request, course_name, day_number):
    getting_id_from_courses_model = Courses_Model.objects.get(Course_name=course_name)
    id_of_course = getting_id_from_courses_model.id
    showing_titles_of_days = Lesson.objects.get(course=id_of_course, day_number=day_number)
    content = showing_titles_of_days.content
    return HttpResponse(content)
        