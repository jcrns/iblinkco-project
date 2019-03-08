from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

User = get_user_model()

# Creating models for social media password for login
class Instagram(models.Model):
    user = models.CharField(max_length=30)
    instagram_username = models.CharField(max_length=30)
    instagram_password = models.CharField(max_length=30)
    number_of_post = models.IntegerField(default=1)
    number_of_followers = models.IntegerField(default=1)
    number_of_following = models.IntegerField(default=1)
    bio = models.TextField(max_length=160, default='unknown')
    location = models.CharField(max_length=30, default='unknown')



    def __str__(self):
        return '{} {}'.format(self.user, self.instagram_username)

class Twitter(models.Model):
    user = models.CharField(max_length=30)
    twitter_username = models.CharField(max_length=30)
    twitter_password = models.CharField(max_length=30)
    number_of_post = models.IntegerField(default=1)
    number_of_followers = models.IntegerField(default=1)
    number_of_following = models.IntegerField(default=1)
    bio = models.TextField(max_length=160, default='unknown')
    location = models.CharField(max_length=30, default='unknown')



    def __str__(self):
        return '{} {}'.format(self.user, self.twitter_username)

class Youtube(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    youtube_username = models.CharField(max_length=30)
    youtube_password = models.CharField(max_length=30)

    def __str__(self):
        return self.youtube_username

class PostSocial(models.Model):
    user = models.CharField(max_length=30)
    text = models.TextField(max_length=280, default='unknown')
    twitter = models.BooleanField()
    instagram = models.BooleanField()
    date = models.DateTimeField(auto_now_add=True)
    viewPast = models.BooleanField(default=True)

    def __str__(self):
        return '{} {}'.format(self.user, self.date)

class LikeOpperation(models.Model):
    user = models.CharField(max_length=30)
    number_of_likes = models.IntegerField(default=1)
    hashtags = models.TextField(max_length=280, default='unknown')
    twitter = models.BooleanField()
    instagram = models.BooleanField()
    date = models.DateTimeField(auto_now_add=True)
    viewPast = models.BooleanField(default=True)

    def __str__(self):
        return '{} {} {}'.format(self.user, self.number_of_likes, self.date)

class FollowOpperation(models.Model):
    user = models.CharField(max_length=30)
    number_of_followers = models.IntegerField(default=1)
    hashtags = models.TextField(max_length=280, default='unknown')
    twitter = models.BooleanField()
    instagram = models.BooleanField()
    date = models.DateTimeField(auto_now_add=True)
    viewPast = models.BooleanField(default=True)


    def __str__(self):
        return '{} {} {}'.format(self.user, self.number_of_followers, self.date)
