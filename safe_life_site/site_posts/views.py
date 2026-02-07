from django.shortcuts import render, redirect
from .models import Branches, Posts, Images
from .form import PostImageDawnlod, PostEdit
from django.utils import timezone

# Create your views here.

#Функция добавения поста
def add_post(request):
    if request.method == "POST":
        post_edit = PostEdit(request.POST, request.FILES)
        post_image = PostImageDawnlod(request.POST, request.FILES)
        if post_edit.is_valid() and post_image.is_valid():
            form = post_edit.save(commit=False)
            form.author = request.user
            form.date = timezone.now()
            form.save()
            return redirect("/")
    else:
        form = PostEdit()
    return render(request, 'post_create.html', {'form':form})