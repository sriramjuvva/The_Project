from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.generic.edit import CreateView
from .forms import RegistrationForm,LoginForm
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from courseapp.urls import * 





class SignUp_View(CreateView):
    template_name = "register.html"
    form_class  = RegistrationForm
    success_url  = reverse_lazy('Login')


class NewLoginPageView(auth_views.LoginView):
    template_name = 'login.html'
    form_class = LoginForm

    def get_success_url(self):
        return reverse_lazy('fetching_the_courses')

    

def home_page_view(request):
    return render(request,'base.html')

