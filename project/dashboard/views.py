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
            userIG = InstagramBot(instagram_post.instagram_username, instagram_post.instagram_password, '')
            messageView = userIG.returnLogin()

            try:
                # User Data
                getUserPost = messageView['userData'][0]
                getUserFollowers = messageView['userData'][1]
                getUserFollowing = messageView['userData'][2]
                getUserBio = messageView['userData'][3]
                message = messageView['message']

                # Saving User Data
                instagram_post.number_of_post = getUserPost
                instagram_post.number_of_followers = getUserFollowers
                instagram_post.number_of_following = getUserFollowing
                instagram_post.bio = getUserBio

                # Getting Ready to return data
                value = {'userPost': getUserPost, 'userFollowers': getUserFollowers, 'userFollowing': getUserFollowing,'userBio':getUserBio, 'message': message}
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
        instagram_post = Instagram()

        instagramInfo = []
        # Using a for loop to get information related to that user

        verify_instagram_post_total = []
        verify_instagram_followers_total = []
        verify_instagram_following_total = []
        for val in INSTAGRAM:
            print("val: ")
            print(val)

            # Getting User Info
            verify_instagram_user = val.user
            verify_instagram_username = val.instagram_username
            verify_instagram_password = val.instagram_password
            verify_instagram_post = val.number_of_post
            verify_instagram_followers = val.number_of_followers
            verify_instagram_following = val.number_of_following
            verify_instagram_bio = val.bio

            if instagram_user_verify == val.user:

                verify_instagram_post_total.append(verify_instagram_post)
                verify_instagram_followers_total.append(verify_instagram_followers)
                verify_instagram_following_total.append(verify_instagram_following)

                value = {'user': verify_instagram_user, 'username': verify_instagram_username, 'userPost': verify_instagram_post, 'userFollowers': verify_instagram_followers, 'userFollowing': verify_instagram_following, 'userBio':verify_instagram_bio, 'totalUserPost':verify_instagram_post_total, 'totalUserFollowers':verify_instagram_post_total, 'totalUserFollowing': verify_instagram_following_total}
                # break'
                instagramInfo.append(value)
        print(value)
        print(instagramInfo)
        return HttpResponse( json.dumps( instagramInfo ))

# Function to disconnect instagram
def InstagramDisconnect(request):
    print("disconnecting user")
    instagram_user_verify = request.POST.get('instagramPostUser')
    selected_option = request.POST.get('selectedOption')
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
            if selected_option == val.instagram_username:
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
            userTwit = twitterBot(twitter_post.twitter_username, twitter_post.twitter_password, '')
            messageView = userTwit.returnLogin()

            try:
                print("trying")
                # User Data
                getUserPost = messageView['userData'][0]
                getUserFollowers = messageView['userData'][1]
                getUserFollowing = messageView['userData'][2]
                getUserBio = messageView['userData'][3]
                getUserLocation = messageView['userData'][4]
                message = messageView['message']

                # Saving User Data
                twitter_post.number_of_post = getUserPost
                twitter_post.number_of_followers = getUserFollowers
                twitter_post.number_of_following = getUserFollowing
                twitter_post.bio = getUserBio
                twitter_post.location = getUserLocation

                # Getting Ready to return data
                value = {'userPost': getUserPost, 'userFollowers': getUserFollowers, 'userFollowing': getUserFollowing,'userBio': getUserBio,'userLocation': getUserLocation, 'message': message}
            except Exception as e:
                print("error")
                message = 'failed'
                value = {'message': message}

            # Checking if function is successful
            print(message)
            if messageView['message'] == 'success':
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
        twitterInfo = []

        # Using a for loop to get information related to that user
        for val in TWITTER:

            # Getting User Info
            verify_twitter_user = val.user
            verify_twitter_username = val.twitter_username
            verify_twitter_post = val.number_of_post
            verify_twitter_followers = val.number_of_followers
            verify_twitter_following = val.number_of_following
            verify_twitter_bio= val.bio
            verify_twitter_location = val.location


            # verify_twitter_post = verify_twitter_post + verify_twitter_post
            if twitter_user_verify in verify_twitter_user:
                print("true")
                print(verify_twitter_user)
                value = {'user': verify_twitter_user, 'username': verify_twitter_username, 'userPost': verify_twitter_post, 'userFollowers': verify_twitter_followers, 'userFollowing': verify_twitter_following, 'userBio':verify_twitter_bio, 'userLocation':verify_twitter_location}

                twitterInfo.append(value)
        return HttpResponse( json.dumps( twitterInfo ))

# Function to disconnect Twitter from database
def TwitterDisconnect(request):
    print("disconnecting user")
    twitter_user_verify = request.POST.get('twitterPostUser')
    selectedOption = request.POST.get('selectedOption')
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
            if selectedOption == val.twitter_username:
                val.delete()
                print("Deleted" + twitter_user_verify + "user")
                break

    value = 'disconnect'
    return HttpResponse(value)

def getTotalSummary(request):
    print("Getting total")
    if request.method == 'POST':
        value = []

        # Getting logged in user
        user_verify = request.POST['usernameVerify']
        print(user_verify)

        content_twitter = Twitter.objects.all()
        TWITTER = content_twitter

        content_instagram = Instagram.objects.all()
        INSTAGRAM = content_instagram

        twitterInfo = []

        # Making variable arrays
        verify_twitter_post_array = []
        verify_twitter_followers_array = []
        verify_twitter_following_array = []

        # Using a for loop to get information related to that user
        for val in TWITTER:

            if user_verify == val.user:
                # Getting User Info
                verify_twitter_user = val.user
                verify_twitter_username = val.twitter_username
                verify_twitter_post = val.number_of_post
                verify_twitter_followers = val.number_of_followers
                verify_twitter_following = val.number_of_following

                print("true")

                print(verify_twitter_post)
                verify_twitter_post_array.append(int(verify_twitter_post))
                verify_twitter_followers_array.append(int(verify_twitter_followers))
                verify_twitter_following_array.append(int(verify_twitter_following))


        sum_verify_twitter_post = sum(verify_twitter_post_array)
        sum_verify_twitter_followers = sum(verify_twitter_followers_array)
        sum_verify_twitter_following = sum(verify_twitter_following_array)
        print(sum_verify_twitter_post, sum_verify_twitter_followers, sum_verify_twitter_following)

        # Making variable arrays
        verify_instagram_post_array = []
        verify_instagram_followers_array = []
        verify_instagram_following_array = []

        for val in INSTAGRAM:

            # Getting User Info
            verify_instagram_user = val.user
            verify_instagram_username = val.instagram_username
            verify_instagram_post = val.number_of_post
            verify_instagram_followers = val.number_of_followers
            verify_instagram_following = val.number_of_following


            if user_verify == verify_instagram_user:
                print("true")

                verify_instagram_post_array.append(int(verify_instagram_post))
                verify_instagram_followers_array.append(int(verify_instagram_followers))
                verify_instagram_following_array.append(int(verify_instagram_following))

        sum_verify_instagram_post = sum(verify_instagram_post_array)
        sum_verify_instagram_followers = sum(verify_instagram_followers_array)
        sum_verify_instagram_following = sum(verify_instagram_following_array)

        sum_post = sum_verify_instagram_post + sum_verify_twitter_post
        sum_followers = sum_verify_instagram_followers + sum_verify_twitter_followers
        sum_following = sum_verify_instagram_following + sum_verify_twitter_following

        value = {'twitterUserPost': sum_verify_twitter_post, 'twitterUserFollowers': sum_verify_twitter_followers, 'twitterUserFollowing': sum_verify_twitter_following, 'instagramUserPost': sum_verify_instagram_post, 'instagramUserFollowers': sum_verify_instagram_followers, 'instagramUserFollowing': sum_verify_instagram_following, 'totalUserPost': sum_post, 'totalUserFollowers': sum_followers, 'totalUserFollowing': sum_following }

        print(value)
        return HttpResponse( json.dumps( value ))

def instagramOnchange(request):
    if request.method == 'POST':
        value = []

        # Getting logged in user
        user_verify = request.POST['usernameVerify']
        user_selected = request.POST['selectedValue']
        print(user_verify)
        content_instagram = Instagram.objects.all()
        INSTAGRAM = content_instagram

        # Using a for loop to get information related to that user
        for val in INSTAGRAM:

            if user_verify == val.user:
                print("user true")
                if user_selected == val.instagram_username:
                    print("user selected")
                    # Getting User Info
                    verify_instagram_user = val.user
                    verify_instagram_username = val.instagram_username
                    verify_instagram_post = val.number_of_post
                    verify_instagram_followers = val.number_of_followers
                    verify_instagram_following = val.number_of_following

                    value = {'user': verify_instagram_user, 'username': verify_instagram_username, 'userPost': verify_instagram_post, 'userFollowers': verify_instagram_followers, 'userFollowing': verify_instagram_following}
        return HttpResponse( json.dumps( value ))

def twitterOnchange(request):
    if request.method == 'POST':
        value = []

        # Getting logged in user
        user_verify = request.POST['usernameVerify']
        user_selected = request.POST['selectedValue']
        print(user_verify)
        content_twitter = Twitter.objects.all()
        TWITTER = content_twitter

        # Using a for loop to get information related to that user
        for val in TWITTER:

            if user_verify == val.user:
                print("user true")
                if user_selected == val.twitter_username:
                    print("user selected")
                    # Getting User Info
                    verify_twitter_user = val.user
                    verify_twitter_username = val.twitter_username
                    verify_twitter_post = val.number_of_post
                    verify_twitter_followers = val.number_of_followers
                    verify_twitter_following = val.number_of_following

                    value = {'user': verify_twitter_user, 'username': verify_twitter_username, 'userPost': verify_twitter_post, 'userFollowers': verify_twitter_followers, 'userFollowing': verify_twitter_following}
        return HttpResponse( json.dumps( value ))

# def postOnSocialScript(content):

def postOnSocial(request):
    print("working")
    if request.method == 'POST':
        # Getting Posted Data
        user_verify = request.POST['opperationPostUser']
        user_caption = request.POST['opperationCaption']
        checkedUsernames = request.POST.getlist('usernames[]')
        if request.POST['opperationPostUser'] and request.POST['opperationCaption'] and request.POST.getlist('usernames[]'):

            # Getting Databases
            content_twitter = Twitter.objects.all()
            TWITTER = content_twitter

            content_instagram = Instagram.objects.all()
            INSTAGRAM = content_instagram

            # Creating array object for verified information
            verified = []
            social_post = PostSocial()

            # For loop
            for val in INSTAGRAM:
                if user_verify == val.user:
                    social_post.user = user_verify
                    for user in checkedUsernames:
                        if user == val.instagram_username:
                            # When user is verified
                            print("true instagram")
                            print(user_caption)
                            social_post.text = user_caption
                            print("insta True!")
                            social_post.instagram = True
                            message = 'success'
                            value = {'message':message}
                            if message != 'success':
                                print("nooo")
                                social_post.instagram = False
                    else:
                        for val2 in TWITTER:
                            if user_verify == val.user:
                                for user in checkedUsernames:
                                    if user == val2.twitter_username:
                                        # When user is verified
                                        print("true twitter")
                                        print(user_caption)
                                        userTwit = twitterBot(val2.twitter_username, val2.twitter_password, user_caption)
                                        messageView = userTwit.postTweet()
                                        social_post.text = user_caption
                                        social_post.twitter = True
                                        message = messageView['message']
                                        if message != 'success':
                                            print("going through if")
                                            message = 'failed'
                                        else:
                                            value = {'message':message}


                                    else:
                                        social_post.twitter = False


            if message == 'success':
                social_post.save()
            print(message)


    return HttpResponse( json.dumps( value ))

def changeBioInstagramOpperation(request):
    if request.method == 'POST':
        instagram_user_verify = request.POST.get('instagramPostUser')
        selected_option = request.POST.get('selectedOption')
        newBio = request.POST.get('newBio')
        if request.POST.get('instagramPostUser') and request.POST.get('selectedOption') and request.POST.get('newBio'):

            # Getting Databases

            content_instagram = Instagram.objects.all()
            INSTAGRAM = content_instagram

            for val in INSTAGRAM:
                if instagram_user_verify == val.user:
                    if selected_option == val.instagram_username:
                        print(selected_option)
                        print("verified")

                        # Adding Instagram Script to verify user is on instagram
                        userIG = InstagramBot(val.instagram_username, val.instagram_password, newBio)
                        messageView = userIG.changeBioReturn()
                        message = messageView['message']

                        if message == 'success':
                            val.bio = newBio
                            val.save()
                            print(val.pk)
                            print(val.bio)
                            value = 'success'
    return HttpResponse(value)


def changeBioTwitterOpperation(request):
    if request.method == 'POST':
        twitter_user_verify = request.POST.get('twitterPostUser')
        selected_option = request.POST.get('selectedOption')
        newBio = request.POST.get('newBio')
        if request.POST.get('twitterPostUser') and request.POST.get('selectedOption') and request.POST.get('newBio'):

            # Getting Databases
            content_twitter = Twitter.objects.all()
            TWITTER = content_twitter

            for val in TWITTER:
                if twitter_user_verify == val.user:
                    if selected_option == val.twitter_username:
                        print(selected_option)
                        print("verified")

                        # Adding Instagram Script to verify user is on instagram
                        userTwit = twitterBot(val.twitter_username, val.twitter_password, newBio)
                        messageView = userTwit.changeBioReturn()
                        message = messageView['message']

                        if message == 'success':
                            val.bio = newBio
                            val.save()
                            print(val.pk)
                            print(val.bio)
                            value = 'success'
    return HttpResponse(value)
