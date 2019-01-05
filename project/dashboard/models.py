from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Creating models for social media password for lgoin
class Instagram(models.Model):
    user = 'davidjr2417'
    instagram_username = models.CharField(max_length=30)
    instagram_password = models.CharField(max_length=30)


    def __str__(self):
        return self.instagram_username

class Twitter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    twitter_username = models.CharField(max_length=30)
    twitter_password = models.CharField(max_length=30)

    def __str__(self):
        return self.twitter_username

class Youtube(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    youtube_username = models.CharField(max_length=30)
    youtube_password = models.CharField(max_length=30)

    def __str__(self):
        return self.youtube_username

# class InstagramPost(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     instagram_username = models.CharField(max_length=30)
#     instagram_password = models.CharField(max_length=30)
#     def __str__(self):
#         return self.instagram_username
#
#     def getUser(self):
#         return self.user
