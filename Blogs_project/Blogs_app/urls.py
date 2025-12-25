from django.urls import path,include
from . import views
from .views import SignUp_View,NewLoginPageView
from django.conf import settings
from django.conf.urls.static import static
from courseapp.views import Courses_to_show


urlpatterns = [
    path("SignUp/",views.SignUp_View.as_view(),name="Signup"),
    path("login/",views.NewLoginPageView.as_view(),name="Login"),
    path('home/', views.home_page_view, name='home'),
    path('courses/courses/', views.Courses_to_show, name='fetching_the_courses'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


