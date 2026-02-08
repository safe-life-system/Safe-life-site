from django.contrib import admin
from django.contrib import admin
from .models import Branches, Posts, Images

# Register your models here.
admin.site.register(Posts)
admin.site.register(Branches)
admin.site.register(Images)