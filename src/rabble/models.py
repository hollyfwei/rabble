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
    