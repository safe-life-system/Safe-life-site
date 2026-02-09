from django.urls import path, re_path
from django.views.generic import TemplateView
from . import views

urlpatterns_posts = [
    path('post_create/', views.add_post, name='post_create'), 
    path('posts/<int:id>/', views.posts, name='posts_data'),
    path('posts_detail/<int:pk>', views.post_detail, name='post_detail')
]