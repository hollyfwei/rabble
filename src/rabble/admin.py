from django.contrib import admin
from .models import User, Community, Follow, Subrabble, Post, Comment, Like, Conversation, Message

admin.site.register(User)
admin.site.register(Community)
admin.site.register(Follow)
admin.site.register(Subrabble)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Conversation)
admin.site.register(Message)
