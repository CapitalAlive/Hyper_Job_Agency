from django.shortcuts import render, redirect, HttpResponse
from . import models
from hyperjob.forms import NewEntry
from django.http import HttpResponseForbidden
from django.contrib.auth.models import User


def resumes(request):
    data = models.Resume.objects.filter()
    return render(request, "entries_list.html", {"data": data})


def new_resume(request):
    if User(request.user).is_staff is False:
        if request.method == "GET":
            return render(request, "new_entry.html", {"object": "Resume", "form": NewEntry})
        elif request.method == "POST":
            models.Resume.objects.create(author=request.user, description=request.POST["description"])
            return redirect("/")
    else:
        return HttpResponseForbidden("")