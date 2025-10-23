from django.urls import path,include
from .views import * 
from . import views

urlpatterns = [
    path('courses/',views.Courses_to_show,name = "courses"),
    path('days/<str:course_name>/',views.fetching_the_content,name = "days"),
    path("content/<str:course_name>/<int:day_number>/",views.fetching_the_content,name="content"),
]

