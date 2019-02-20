from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

User = get_user_model()

# Creating models for social media password for login
class Instagram(models.Model):
    user = models.CharField(max_length=30)
    instagram_username = models.CharField(max_length=30)
    instagram_password = models.CharField(max_length=30)

    def __str__(self):
        return '{} {}'.format(self.user, self.instagram_username)

class Twitter(models.Model):
    user = models.CharField(max_length=30)
    twitter_username = models.CharField(max_length=30)
    twitter_password = models.CharField(max_length=30)

    def __str__(self):
        return '{} {}'.format(self.user, self.twitter_username)

class Youtube(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    youtube_username = models.CharField(max_length=30)
    youtube_password = models.CharField(max_length=30)

    def __str__(self):
        return self.youtube_username
