from django.urls import path, re_path
from django.views.generic import TemplateView
from . import views

urlpatterns_posts = [
    path('post_create/', views.add_post, name='post_create'), 
    path('posts/<slug:slug>/', views.posts, name='posts_data'),
    path('posts_detail/<slug:slug>', views.post_detail, name='post_detail'),
    path('post/editer/<slug:slug>', views.post_edit, name='post_edit')
]