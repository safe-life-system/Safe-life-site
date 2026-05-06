from django.db import models
from site_posts.models import Posts
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Comments(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    user_name = models.ForeignKey(User, models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.text