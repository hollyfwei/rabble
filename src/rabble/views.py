from django.shortcuts import render, redirect, reverse, get_object_or_404   
from django.http import HttpResponse
from django.contrib.auth import logout
from .models import Subrabble, Community, Post
from .forms import PostForm

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

def post_detail(request, identifier, pk):
    subrabble = Subrabble.objects.get(identifier=identifier)
    post = subrabble.posts.get(pk=pk)
    comments = post.comments.all()
    return render(request, "rabble/post_detail.html", 
                  {"subrabble": subrabble, 
                   "post": post , 
                   "comments": comments})

def post_create(request, identifier):
    subrabble = Subrabble.objects.get(identifier=identifier)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('subrabble-detail', identifier=subrabble.identifier))
    else:
        form = PostForm()
    return render(request, "rabble/post_form.html", {"form": form, "subrabble": subrabble})

def post_edit(request, identifier, pk):
    subrabble = Subrabble.objects.get(identifier=identifier)
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect(reverse('post-detail', identifier=subrabble.identifier, pk=post.pk))
    else:
        form = PostForm(instance=post)
    return render(request, "rabble/post_form.html", {"form": form, "subrabble": subrabble})