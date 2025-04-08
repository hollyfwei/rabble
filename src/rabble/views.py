from django.shortcuts import render, redirect    
from django.http import HttpResponse
from django.contrib.auth import logout

def index(request):
    context = {"welcome": "Hello, world!"}

    return render(request, "rabble/index.html", context)

def profile(request):
    return render(request, "rabble/profile.html")