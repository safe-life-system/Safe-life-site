from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from slugify import slugify

def user_directory_path(instance, filename):
    try:
        return f'{instance.branche.name_branche}/{instance.author.username}/{timezone.now().date()}/{filename}'
    except:
        return f'{instance.posts.branche.name_branche}/{instance.posts.author.username}/{timezone.now().date()}/{filename}'

# Create your models here.
class Branches(models.Model):
    name_branche = models.CharField(max_length=50)
    category = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True, null=True, allow_unicode=True)
    
    def __str__(self):
        return self.name_branche
    
    def get_absolute_url(self):
        return reverse('posts_data', kwargs={'slug': self.slug})
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name_branche)
        return super().save(*args, **kwargs)

class Posts(models.Model):
    branche = models.ForeignKey(Branches, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title_image = models.ImageField(upload_to=user_directory_path, blank=True)
    title = models.CharField(max_length=200)
    main_text = models.TextField()
    text = models.TextField(blank=True)
    file = models.FileField(upload_to=user_directory_path, blank=True)
    date = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(unique=True, blank=True, null=True, allow_unicode=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

class Images(models.Model):
    posts = models.ForeignKey(Posts, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=user_directory_path, blank=True)