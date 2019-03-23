from django.conf.urls import url, include
from . import views
from django.views.generic import RedirectView

# Connecting views to dash with urls
urlpatterns = [
    # Index view
    url(r'^$', views.index, name='dash.index'),

    #Ajax Python functions

    # instagram functions
    url(r'^instagram-account-disconnect$', views.InstagramDisconnect, name='disconnect-instagram/'),
    url(r'^instagram-onchange$', views.instagramOnchange, name='instagram-onchange/'),
    url(r'^instagram-bio-change$', views.changeBioInstagramOpperation, name='change-bio-instagram/'),

    # twitter functions
    url(r'^twitter-account-disconnect$', views.TwitterDisconnect, name='disconnect-twitter/'),
    url(r'^twitter-onchange$', views.twitterOnchange, name='twitter-onchange/'),
    url(r'^twitter-bio-change$', views.changeBioTwitterOpperation, name='change-bio-twitter/'),

    # other functions
    url(r'^account-posting$', views.postSocial, name='create-social/'),
    url(r'^account-check$', views.check, name='check-out/'),
    url(r'^get-total-summary$', views.getTotalSummary, name='get-total-summary/'),
    url(r'^post-on-social$', views.postOnSocial, name='post-on-social/'),
    url(r'^auto-like-favorite$', views.autoLikes, name='auto-like-social/'),
    url(r'^auto-follow$', views.autoFollow, name='auto-follow-social/'),
    url(r'^get-opperation-history$', views.getOpperationHistory, name='get-opperation-history/'),
    url(r'^clear-opperation-history$', views.clearOpperationHistory, name='clear-opperation-history/'),



]
