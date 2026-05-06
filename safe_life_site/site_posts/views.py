from django.shortcuts import render, redirect, get_object_or_404

from .models import Branches, Posts, Images
from .form import PostImageDawnlod, PostEdit
from django.utils import timezone
import markdown
from django.utils.text import slugify
from site_users.forms import AddComment
from site_users.models import Comments

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
            for file in request.FILES.getlist('image'):
                Images.objects.create(posts=form, image=file)
            return redirect("/")
    else:
        form = PostEdit()
        form_image = PostImageDawnlod()
    return render(request, 'post_create.html', {'form':form, 'form_image':form_image})

#Функция вывода постов
def posts(request, slug):
    branche = get_object_or_404(Branches, slug = slug)
    posts_data = Posts.objects.filter(branche__name_branche=branche).order_by('-date')
    for post in posts_data:
        post.main_text = markdown.markdown(post.main_text, extensions=['fenced_code', 'codehilite'])
    return render(request, 'posts.html', {'branche': branche,'posts': posts_data})

#Функция вывода деталей поста
def post_detail(request, slug):
    post = get_object_or_404(Posts, slug=slug)
    post.main_text = markdown.markdown(post.main_text, extensions=['fenced_code', 'codehilite'])
    post.text = markdown.markdown(post.text, extensions=['fenced_code', 'codehilite'])
    image = Images.objects.filter(posts=post)
    comment = Comments.objects.filter(post=post).order_by("-date")
    form = AddComment()
    return render(request, "post_detail.html", {'post':post, 'image':image, 'comments':comment, 'comment_form':form})

def post_edit(request, slug):
    post = get_object_or_404(Posts, slug=slug)
    if request.method == "POST":
        form_post = PostEdit(request.POST, request.FILES, instance=post)
        form_image = PostImageDawnlod(request.POST, request.FILES, instance=post)
        if form_post.is_valid() and form_image.is_valid():
            form = form_post.save(commit=False)
            form.author = request.user
            form.date = timezone.now()
            form.save()
            for file in request.FILES.getlist('image'):
                Images.objects.create(posts=form, image=file)
            return redirect('post_detail', slug=post.slug)
    form = PostEdit(instance=post)
    form_image = PostImageDawnlod(instance=post)
    return render(request, 'post_create.html', {'form':form, 'form_image':form_image})

#Редирект старых url постов 
def old_posts_redirect(request, pk):
    branche = Branches.objects.filter(pk=pk).first()

    if branche:
        return redirect(branche.get_absolute_url(), permanent=True)

    return redirect('/', permanent=True)

#Редирект старых url поста
def old_post_detail_redirect(request, pk):
    post = Posts.objects.filter(pk=pk).first()

    if post:
        return redirect(post.get_absolute_url(), permanent=True)

    return redirect('/', permanent=True)

#Функция ввыода комментария
def enter_comment(request, slug):
    post = get_object_or_404(Posts, slug=slug)
    
    if request.method == "POST":
        form = AddComment(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user_name = request.user
            comment.save()

            return render(request, "comment.html", {
                "comment": comment,
            })
    return render(request, "comment.html", {"comment": comment,})