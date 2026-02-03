from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserReg

# Create your views here.

def user_regiistration(request):
    if request.method == 'POST':
        form = UserReg(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(request, username=request.POST.get("username"), password=request.POST.get("password1"))
            if user is not None:
                login(request=request, user=user)
                return redirect('/')
    form = UserReg()
    return render(request, "user_registration/user_registration.html", {"user_form":form})

def user_login(request):
    if request.method == 'POST':
        user_name = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=user_name, password=password)
        if user is not None:
            login(request=request, user=user)
            return redirect('/')
    return render(request, "user_registration/user_login.html")