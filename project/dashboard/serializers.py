# serializer class converting django model data into useful data able to be transfered
from rest_framework import serializers

# Importing models
from dashboard.models import *

from django.contrib.auth import *

# naming classes after classes imported from models
class InstagramSerializer(serializers.ModelSerializer):

    class Meta:
        model = Instagram
        fields = '__all__'

    # Validating for simular username to avoid duplicates
    def validate_title(self, value):
        qs = Instagram.objects.filter(instagram_username__iexact=value) # including instance
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("This title has already been used")
        return value


class TwitterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Twitter
        fields = '__all__'

class YoutubeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Youtube
        fields = '__all__'
