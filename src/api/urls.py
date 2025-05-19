from django.urls import path

from . import views

urlpatterns = [
    path('subrabbles/', views.subrabble_list, name='api-subrabble-list'),
    path('subrabbles/!<str:identifier>', views.subrabble_detail, name='api-subrabble-detail'),
    path('subrabbles/!<str:identifier>/posts', views.PostList.as_view(), name='api-post-list'),
    path('subrabbles/!<str:identifier>/posts/<int:pk>', views.PostDetail.as_view(), name='api-post-detail')
]