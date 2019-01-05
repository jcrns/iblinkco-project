# serializer class converting django model data into useful data able to be transfered
from rest_framework import serializers

# Importing models
from dashboard.models import *

from django.contrib.auth import *

# naming classes after classes imported from models
class InstagramSerializer(serializers.ModelSerializer):

    class Meta:
        model = Instagram
        fields = 'instagram_username'

class TwitterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Twitter
        fields = 'twitter_username'

class YoutubeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Youtube
        fields = ('youtube_username')
