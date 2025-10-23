from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from .models import *
from . import serializers 
from . serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.

@api_view(['GET'])
def Courses_to_show(request):
    all_courses = Courses_Model.objects.all().order_by('id')  # simpler than raw()
    serializer = courseserializer(all_courses, many=True)
    print(serializer.instance,"000000000000000000000000000")
    return Response(serializer.data)