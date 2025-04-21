from django.shortcuts import render, redirect    
from django.http import HttpResponse
from django.contrib.auth import logout
from .models import Subrabble, Community

def index(request):
    default_com = Community.objects.get(community_name="default")
    subrabbles = Subrabble.objects.filter(community=default_com)
    return render(request, "rabble/index.html", {"subrabbles": subrabbles})

def profile(request):
    return render(request, "rabble/profile.html")

def subrabble_detail(request, identifier):
    subrabble = Subrabble.objects.get(identifier=identifier)
    posts = subrabble.posts.all()
    return render(request, "rabble/subrabble_detail.html", 
                  {"subrabble": subrabble, "posts": posts})