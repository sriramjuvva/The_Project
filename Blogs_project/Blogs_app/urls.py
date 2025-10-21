from django.urls import path,include
from . import views
from .views import *


urlpatterns = [
    path("SignUp/",views.SignUp_View.as_view()),
    path("login/",views.NewLoginPageView.as_view(),name="Login"),
     path('home/', views.home_page_view, name='home'),
]


