from django.urls import path
from . import views
urlpatterns = [
    path("login", views.Login.as_view(), name="login_url"),
    path("logout", views.Logout.as_view(), name="logout_url"),
    path("signup", views.Signup.as_view(), name="signup_url"),
]
