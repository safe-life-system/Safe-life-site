from django.contrib.sitemaps import Sitemap
from .models import Posts, Branches
from django.conf import settings

class PostsSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Posts.objects.all().order_by('-date')

    def lastmod(self, obj):
        return obj.date

class BranchesSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.6

    def items(self):
        return Branches.objects.all()