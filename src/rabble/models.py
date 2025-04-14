from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    user_id = models.IntegerField(primary_key=True)
    profile_picture = models.TextField(blank=True, null=True)
    short_bio = models.TextField(blank=True, null=True)
    interests = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ('username', 'email')

class Community(models.Model):
    community_id = models.IntegerField(primary_key=True)
    community_name = models.TextField(unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

class Subrabble(models.Model):
    class Visibility(models.IntegerChoices):
        PUBLIC = 1, "Public"
        PRIVATE = 2, "Private"
    visibility = models.PositiveSmallIntegerField(choices=Visibility.choices, default=Visibility.PUBLIC)
    subrabble_id = models.IntegerField(primary_key=True)
    community_id = models.ForeignKey(Community, on_delete=models.CASCADE)
    subrabble_name = models.TextField(unique=True)
    description = models.TextField()
    anonymous_permissions = models.BooleanField(default=False)

    class Meta:
        unique_together = ('community_id', 'subrabble_name')

class Post(models.Model):
    post_id = models.IntegerField(primary_key=True)
    subrabble_id = models.ForeignKey(Subrabble, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField()
    body = models.TextField()
    anonymity = models.BooleanField(default=False)

class Comment(models.Model):
    comment_id = models.IntegerField(primary_key=True)
    parent_id = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    anonymity = models.BooleanField(default=False)

class Like(models.Model):
    class LikeableType(models.IntegerChoices):
        POST = 1, "Post"
        COMMENT = 2, "Comment"
    likeable_type = models.PositiveSmallIntegerField(choices=LikeableType.choices, default=LikeableType.POST)
    like_id = models.IntegerField(primary_key=True)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    comment_id = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, blank=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class Conversation(models.Model):
    conversation_id = models.IntegerField(primary_key=True)
    community_id = models.ForeignKey(Community, on_delete=models.CASCADE)
    title = models.TextField()

class Message(models.Model):    
    message_id = models.IntegerField(primary_key=True)
    conversation_id = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    