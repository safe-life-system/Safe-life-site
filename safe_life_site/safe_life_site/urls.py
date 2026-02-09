"""
URL configuration for safe_life_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from site_users.views import user_regiistration
from site_users.urls import urlpatterns
from site_posts.urls import urlpatterns_posts
from django.contrib.sitemaps.views import sitemap
from site_posts.sitemaps import PostsSitemap
from django.conf import settings
from django.conf.urls.static import static

sitemaps = {
    'posts': PostsSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="main.html")),
    path('manager-passwords/', TemplateView.as_view(template_name="error.html")),
    path('messenger/', TemplateView.as_view(template_name="error.html")),
    path('forum/', TemplateView.as_view(template_name="error.html")),
    path('core/', TemplateView.as_view(template_name="error.html")),
    path('accaunt/', include(urlpatterns)),
    path('post/', include(urlpatterns_posts)),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)