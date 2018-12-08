import sys
# Linking tweepy file
sys.path.append('/Users/hgpmac87/Desktop/iblinkco-project/project/dashboard/twitter-api')
import tweepy_streamer

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Linking Twitter file and Printing Twitter Data on Webpage
twitter = tweepy_streamer #.TweetAnalyzer()

# Requiring a login in order to accessing page
@login_required
def index(request):
    return render(request, 'dashboard/home.html', {'content':{'twit':'twitter information', 'twitter':twitter}})
