from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import HttpResponse, redirect


def index(request):
    return render(request, "index.html")


def home(request):
    print(User(username=request.user).is_staff)
    if request.user.is_staff:
        return redirect("/vacancy/new")
    else:
        return redirect("/resume/new")
