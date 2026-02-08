from django.shortcuts import render

from .models import Branches

# Create your views here.

def branches_processor(request):
    branche_data = Branches.objects.all()
    return {"branches": branche_data}