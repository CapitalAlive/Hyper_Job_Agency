from django.urls import path
from . import views

urlpatterns = [
    path("vacancies", views.vacancies, name="vacancies_url"),
    path("vacancy/new", views.new_vacancy, name="new_vacancy_url")

]