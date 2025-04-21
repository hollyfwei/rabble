from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("profile/", views.profile, name="profile"),
    path("!<slug:identifier>/", views.subrabble_detail, name="subrabble-detail")
]