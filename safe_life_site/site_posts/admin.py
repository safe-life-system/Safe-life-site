from django.contrib import admin
from django.contrib import admin
from .models import Branches, Posts, Images
from site_users.models import Comments

# Register your models here.
admin.site.register(Posts)
admin.site.register(Branches)
admin.site.register(Images)
admin.site.register(Comments)