from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
# Create your views here.

class Signup(CreateView):
    form_class = UserCreationForm
    success_url = "/login"
    template_name = "signup.html"

class Login(LoginView):
    success_url = ""
    template_name = "login.html"
    redirect_authenticated_user = True

class Logout(LogoutView):
    template_name = "logout.html"
    http_method_names = ["post", "get"]
