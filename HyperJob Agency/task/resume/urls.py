from django.urls import path
from . import views
urlpatterns = [
    path("resumes", views.resumes, name="resumes_url"),
    path("resume/new", views.new_resume, name="new_resume_url"),
]