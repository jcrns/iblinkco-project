import sys

# Importing login_required function from django
from django.contrib.auth.decorators import login_required

#Rest API requesting data from Database
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from dashboard.serializer import *
from dashboard.models import *
# importing django render
from django.shortcuts import render

# API in View
class InstagramList(APIView):

    def get(self, request):
        instagram = Instagram.objects.all()
        serializers = InstagramSerializer(instagram)
        return Response(serializers.data)

    def post(self):
        pass

# Importing twitter file
sys.path.append('/users/hgpmac87/desktop/iblinkco-project/project/dashboard/api/twitter-api')
import tweepy_streamer

# Importing facebook file
sys.path.append('/users/hgpmac87/desktop/iblinkco-project/project/dashboard/api/facebook-api')
import facebook_getdata

# # Importing instagram file
sys.path.append('/users/hgpmac87/desktop/iblinkco-project/project/dashboard/api/instagram-api')
import instagram_getdata

# # Importing youtube file
# sys.path.append('/users/hgpmac87/desktop/iblinkco-project/project/dashboard/api/youtube-api')
# import youtube_getdata


# Creating Variables set to the api files
twitter = tweepy_streamer
instagram = instagram_getdata

# Requiring a login in order to accessing page
@login_required
def index(request):
    return render(request, 'dashboard/home.html', {'content':{'twitter':twitter, 'instagram':instagram}})
