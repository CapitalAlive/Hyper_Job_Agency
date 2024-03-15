from django.shortcuts import render, redirect, HttpResponse
from . import models
from django.http import HttpResponseForbidden
from hyperjob.forms import NewEntry
from django.contrib.auth.models import User


def vacancies(request):
    data = models.Vacancy.objects.filter()
    return render(request, "entries_list.html", {"data": data})


def new_vacancy(request):
    if request.user.is_staff:
        if request.method == "GET":
            return render(request, "new_entry.html", {"object": "Vacancy", "form": NewEntry})
        elif request.method == "POST":
            models.Resume.objects.create(author=request.user, description=request.POST["description"])
    else:
        return HttpResponseForbidden()

