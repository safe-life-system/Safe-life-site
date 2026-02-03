from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path("registration/", views.user_regiistration, name="user_registration"),
    path("login/", views.user_login, name="user_login"),
]