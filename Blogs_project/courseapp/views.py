from django.shortcuts import render
from django.http import JsonResponse,HttpResponse,FileResponse
from .models import *
from . import serializers 
from . serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower



# Create your views here.

@api_view(['GET'])
def Courses_to_show(request):
    all_courses = Courses_Model.objects.all().order_by('id')  # simpler than raw()
    serializer = courseserializer(all_courses, many=True)
    context = {'courses': serializer.data}
    return render(request, 'base.html', context)



@api_view(['GET'])
def fetching_the_days(request,course_name):
    course = (
        Courses_Model.objects.annotate(lower_name=Lower('Course_name')).filter(lower_name=course_name.lower()).first())
    if not course:
        return HttpResponse("Oops! There is no course with that name.")
    lesson = Lesson.objects.filter(course=course).first()
    if not lesson:
        return HttpResponse("No lessons found for this course.")
    return HttpResponse(f"{lesson.day_number} - {lesson.title}")


@login_required(login_url='/Users/login/')
def fetching_the_content(request, course_name, day_number):
    course = Courses_Model.objects.annotate(lower_name=Lower('Course_name')).filter(lower_name=course_name.lower()).first()
    if not course:
        return JsonResponse({"Success": False, "Message": "No Courses Found"})
    lesson = Lesson.objects.filter(course=course, day_number=day_number).first()
    if not lesson:
        return HttpResponse("The Course is not updated for that date")
    return HttpResponse(lesson.content or "Coming Soon")