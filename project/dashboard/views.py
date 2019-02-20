import sys
import json

# Importing login_required function from django
from django.contrib.auth.decorators import login_required

# Importing Http Response
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect, JsonResponse

# Rest API requesting data from Database
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from dashboard.serializers import *
from dashboard.models import *

# Importing forms for custom forms
from dashboard.forms import *

# importing django render
from django.shortcuts import render

# Importing Scripts to verify users
from dashboard.instagram_script import *
from dashboard.twitter_script import *

# API in View
class InstagramList(APIView):

    def get(self, request):
        instagram = Instagram.objects.all()
        serializers = InstagramSerializer(instagram, many=True)
        return Response(serializers.data)

    def post(self):
        pass


# Requiring a login in order to accessing page
@login_required
def index(request):
    content = {}
    return render(request, 'dashboard/home.html', content)

## INSTAGRAM ##

def InstagramPost(request):
    print("Starting Post")
    if request.method == 'POST':
        print("this is finally working")

        print(request.POST.get('instagramPostUser'))
        print(request.POST.get('instagramUsername'))
        print(request.POST.get('instagramPassword'))

        if request.POST.get('instagramPostUser') and request.POST.get('instagramUsername') and request.POST.get('instagramPassword'):

            instagram_post = Instagram()
            instagram_post.user = request.POST.get('instagramPostUser')
            instagram_post.instagram_username = request.POST.get('instagramUsername')
            instagram_post.instagram_password = request.POST.get('instagramPassword')

            # Success Variable
            value = True
            print("worrrks")


            # Adding Instagram Script to verify user is on instagram
            userIG = InstagramBot(instagram_post.instagram_username, instagram_post.instagram_password)
            messageView = userIG.login()
            message = messageView['message']

            try:
                # User Data
                getUserPost = messageView['userData'][0]
                getUserFollowers = messageView['userData'][1]
                getUserFollowing = messageView['userData'][2]

                # Saving User Data
                instagram_post.number_of_post = getUserPost
                instagram_post.number_of_followers = getUserFollowers
                instagram_post.number_of_following = getUserFollowing

                # Getting Ready to return data
                value = {'userPost': getUserPost, 'userFollowers': getUserFollowers, 'userFollowing': getUserFollowing, 'message': message}
            except Exception as e:
                print("error")
                message = 'failed'
                value = {'message': message}

            # Checking if function is successful
            if message == 'success':
                # Saving Form
                instagram_post.save()

            print(value)
        return HttpResponse( json.dumps( value ))

# Function to check if signed in user has a instagram account
def InstagramCheck(request):
    print("Checking if user has instagram accounts")
    if request.method == 'POST':
        value = []
        # Getting logged in user
        instagram_user_verify = request.POST['instagram_user']
        print(instagram_user_verify)

        content_instagram = Instagram.objects.all()
        INSTAGRAM = content_instagram
        print(INSTAGRAM)
        # Using a for loop to get information related to that user
        for val in INSTAGRAM:
            print(val)

            # Getting User Info
            verify_instagram_user = val.user
            verify_instagram_username = val.instagram_username
            verify_instagram_post = val.number_of_post
            verify_instagram_followers = val.number_of_followers
            verify_instagram_following = val.number_of_following

            if instagram_user_verify in verify_instagram_user:
                print("true")
                print(verify_instagram_user)
                value = {'user': verify_instagram_user, 'username': verify_instagram_username, 'userPost': verify_instagram_post, 'userFollowers': verify_instagram_followers, 'userFollowing': verify_instagram_following}
                break
        print(value)
        return HttpResponse( json.dumps( value ))

# Function to disconnect instagram
def InstagramDisconnect(request):
    print("disconnecting user")
    instagram_user_verify = request.POST.get('instagramPostUser')
    content_instagram = Instagram.objects.all()
    INSTAGRAM = content_instagram
    for val in INSTAGRAM:
        verify_instagram_user = val.user
        verify_instagram_user_final = str(verify_instagram_user)
        verify_instagram_user_final2 = str(instagram_user_verify)
        print(verify_instagram_user_final)
        print(verify_instagram_user_final2)

        print(verify_instagram_user_final2 == verify_instagram_user_final)
        if instagram_user_verify == verify_instagram_user:
            val.delete()
            print("Deleted" + instagram_user_verify + "user")
            break

    value3 = 'disconnect'
    return HttpResponse(value3)

## TWITTER ##

# twitter post function
def TwitterPost(request):
    print("Starting Post Twitter")
    if request.method == 'POST':
        print("this is finally working")

        print(request.POST.get('twitterPostUser'))
        print(request.POST.get('twitterUsername'))
        print(request.POST.get('twitterPassword'))

        if request.POST.get('twitterPostUser') and request.POST.get('twitterUsername') and request.POST.get('twitterPassword'):

            twitter_post = Twitter()
            twitter_post.user = request.POST.get('twitterPostUser')
            twitter_post.twitter_username = request.POST.get('twitterUsername')
            twitter_post.twitter_password = request.POST.get('twitterPassword')

            # Adding Instagram Script to verify user is on instagram
            userTwit = twitterBot(twitter_post.twitter_username, twitter_post.twitter_password)
            messageView = userTwit.login()
            message = messageView['message']

            try:
                # User Data
                getUserPost = messageView['userData'][0]
                getUserFollowers = messageView['userData'][1]
                getUserFollowing = messageView['userData'][2]

                # Saving User Data
                twitter_post.number_of_post = getUserPost
                twitter_post.number_of_followers = getUserFollowers
                twitter_post.number_of_following = getUserFollowing

                # Getting Ready to return data
                value = {'userPost': getUserPost, 'userFollowers': getUserFollowers, 'userFollowing': getUserFollowing, 'message': message}
            except Exception as e:
                print("error")
                message = 'failed'
                value = {'message': message}

            # Checking if function is successful
            if message == 'success':
                # Saving Form
                twitter_post.save()

        return HttpResponse( json.dumps( value ))


# Function to check if signed in user has a twitter account
def TwitterCheck(request):
    print("Checking if user has twitter accounts")
    if request.method == 'POST':
        value = []

        # Getting logged in user
        twitter_user_verify = request.POST['twitter_user']
        print(twitter_user_verify)

        content_twitter = Twitter.objects.all()
        TWITTER = content_twitter

        # Using a for loop to get information related to that user
        for val in TWITTER:

            # Getting User Info
            verify_twitter_user = val.user
            verify_twitter_username = val.twitter_username
            verify_twitter_post = val.number_of_post
            verify_twitter_followers = val.number_of_followers
            verify_twitter_following = val.number_of_following

            if twitter_user_verify in verify_twitter_user:
                print("true")
                print(verify_twitter_user)
                value = {'user': verify_twitter_user, 'username': verify_twitter_username, 'userPost': verify_twitter_post, 'userFollowers': verify_twitter_followers, 'userFollowing': verify_twitter_following}
                break
        print(value)
        return HttpResponse( json.dumps( value ))

# Function to disconnect Twitter from database
def TwitterDisconnect(request):
    print("disconnecting user")
    twitter_user_verify = request.POST.get('twitterPostUser')
    content_twitter = Twitter.objects.all()
    TWITTER = content_twitter
    for val in TWITTER:
        verify_twitter_user = val.user
        verify_twitter_user_final = str(verify_twitter_user)
        verify_twitter_user_final2 = str(twitter_user_verify)
        print(verify_twitter_user_final)
        print(verify_twitter_user_final2)

        print(verify_twitter_user_final2 == verify_twitter_user_final)
        if twitter_user_verify == verify_twitter_user:
            val.delete()
            print("Deleted" + twitter_user_verify + "user")
            break

    value3 = 'disconnect'
    return HttpResponse(value3)
