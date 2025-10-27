from django.urls import path,include
from . import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("SignUp/",views.SignUp_View.as_view(),name="Signup"),
    path("login/",views.NewLoginPageView.as_view(),name="Login"),
     path('home/', views.home_page_view, name='home'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


