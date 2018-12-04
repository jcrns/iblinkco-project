import sys
sys.path.append('/Users/hgpmac87/Desktop/iblinkco-project/project/dashboard/twitter-api')
import tweepy_streamer

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

twitter = tweepy_streamer.TweetAnalyzer()

@login_required
def index(request):
    return render(request, 'dashboard/home.html', {'content':['twitter information', twitter]})
