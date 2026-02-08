from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path("registration/", views.user_regiistration, name="user_registration"),
    path("login/", views.user_login, name="user_login"),
    path("", TemplateView.as_view(template_name="user_accaunt/user_accaunt.html"), name="user_accaunt")
]