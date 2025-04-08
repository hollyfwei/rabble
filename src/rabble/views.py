from django.shortcuts import render, redirect    
from django.http import HttpResponse

def index(request):
    context = {"welcome": "Hello, world!"}

    return render(request, "rabble/index.html", context)

def profile(request):
    return render(request, "rabble/profile.html")

def logout(request):
    logout(request)
    return redirect('index')