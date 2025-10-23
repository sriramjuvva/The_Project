from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django_recaptcha.fields import ReCaptchaField
from django import forms
from .models import CustomUser
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate


class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=50, required=False,label="Username")
    first_name =forms.CharField(max_length=50, required=False,label = "first_name")
    last_name = forms.CharField(max_length=50, required=False,label = "last_name")
    email = forms.CharField(max_length=50, required=True,label = "Email")
    
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if CustomUser.objects.filter(username = username).exists():
            raise ValidationError("Username Already exists")
        return username

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user

        

class LoginForm(AuthenticationForm):
    captcha = ReCaptchaField()
    class Meta:
        fields = ['username', 'password', 'captcha']


    def __init__(self, *args, **kwargs):
        self.request = kwargs.get("request", None)
        if self.request is None:
            raise ValueError("Request is required for this form")
        super().__init__(*args, **kwargs)

    def clean(self):
        # Fetch the data from the form fields
        username = self.cleaned_data.get('username')  # 'username' is used as the email
        password = self.cleaned_data.get('password')

        # Custom validation for email and password
        if username and password:
            # Check if the user exists in the database
            try:
                user = CustomUser.objects.get(username=username)
            except CustomUser.DoesNotExist:
                raise ValidationError("username not found. Please enter a valid Username.")

            # Authenticate the user
            user = authenticate(self.request, username=username, password=password)
            if user is None:
                raise ValidationError("Invalid email or password. Please try again.")

            # Check if the user is active
            if not user.is_active:
                raise ValidationError("Your account is inactive. Please contact support.")
        else:
            raise ValidationError("Both email and password are required.")

        # Optionally return the cleaned data (no need to call super().clean())
        return self.cleaned_data

    def get_user(self):
        return getattr(self, 'user_cache', None)