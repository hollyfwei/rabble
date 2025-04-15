from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    profile_picture = models.TextField(blank=True, null=True)
    short_bio = models.TextField(blank=True, null=True)
    interests = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ('username', 'email')
    
    def __str__(self):
        return self.username

class Community(models.Model):
    community_name = models.TextField(unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    users = models.ManyToManyField(User, related_name='communities', blank=True)

    def __str__(self):
        return self.community_name

class Follow(models.Model):
    followee = models.ForeignKey(User, related_name='followees', on_delete=models.CASCADE)
    follower = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('followee', 'follower')

    def __str__(self):
        return f"{self.follower.username} follows {self.followee.username}"
    
class Subrabble(models.Model):
    class Visibility(models.IntegerChoices):
        PUBLIC = 1, "Public"
        PRIVATE = 2, "Private"
    visibility = models.PositiveSmallIntegerField(choices=Visibility.choices, default=Visibility.PUBLIC)

    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    subrabble_name = models.TextField(unique=True)
    description = models.TextField()
    anonymous_permissions = models.BooleanField(default=False)
    users = models.ManyToManyField(User, related_name='subrabble_users', blank=True)

    class Meta:
        unique_together = ('community', 'subrabble_name')

    def __str__(self):
        return f"{self.subrabble_name} in {self.community.community_name}"

class Post(models.Model):
    subrabble = models.ForeignKey(Subrabble, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField()
    body = models.TextField()
    anonymity = models.BooleanField(default=False)

    def __str__(self):
        if self.anonymity:
            return f"Anonymous Post in {self.subrabble.subrabble_name}: {self.title}"
        else:
            return f"Post by {self.user.username} in {self.subrabble.subrabble_name}: {self.title}"

class Comment(models.Model):
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    anonymity = models.BooleanField(default=False)

    def __str__(self):
        if self.anonymity:
            return f"Anonymous Comment on Post {self.post.post_id}: {self.body}"
        else:
            return f"Comment by {self.user.username} on Post {self.post.post_id}: {self.body}"
        
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, blank=True)
    
    class LikeableType(models.IntegerChoices):
        POST = 1, "Post"
        COMMENT = 2, "Comment"
    likeable_type = models.PositiveSmallIntegerField(choices=LikeableType.choices, default=LikeableType.POST)
    
    class Meta:
        constraints = [
            # Ensure only one of post or comment is liked
            models.CheckConstraint(
                check=(
                    models.Q(post__isnull=False, comment__isnull=True) |
                    models.Q(post__isnull=True, comment__isnull=False)
                ),
                name='like_either_post_or_comment'
            ),
            # Unique like per user/post
            models.UniqueConstraint(
                fields=['user', 'post'],
                name='unique_like_per_user_post',
                condition=models.Q(post__isnull=False)
            ),
            # Unique like per user/comment
            models.UniqueConstraint(
                fields=['user', 'comment'],
                name='unique_like_per_user_comment',
                condition=models.Q(comment__isnull=False)
            ),
        ]

    def __str__(self):
        if self.post:
            return f"Like on Post {self.post.post_id} by {self.user.username}"
        elif self.comment:
            return f"Like on Comment {self.comment.comment_id} by {self.user.username}"

class Conversation(models.Model):
    community_id = models.ForeignKey(Community, on_delete=models.CASCADE)
    title = models.TextField()
    users = models.ManyToManyField(User, related_name='conversations', blank=True)

    def __str__(self):
        return self.title

class Message(models.Model):    
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.user.username} ({self.timestamp}): {self.text}..."
    