from django.conf.urls import url, include
from . import views
from django.views.generic import RedirectView

# Connecting views to dash with urls
urlpatterns = [
    # Index view
    url(r'^$', views.index, name='dash.index'),

    #Ajax Python functions

    # instagram functions
    url(r'^instagram-posting$', views.InstagramPost, name='instagram-post/'),
    url(r'^instagram-account-check$', views.InstagramCheck, name='check-out-instagram/'),
    url(r'^instagram-account-disconnect$', views.InstagramDisconnect, name='disconnect-instagram/'),
    url(r'^instagram-onchange$', views.instagramOnchange, name='instagram-onchange/'),


    # twitter functions
    url(r'^twitter-posting$', views.TwitterPost, name='twitter-post/'),
    url(r'^twitter-account-check$', views.TwitterCheck, name='check-out-twitter/'),
    url(r'^twitter-account-disconnect$', views.TwitterDisconnect, name='disconnect-twitter/'),
    url(r'^twitter-onchange$', views.twitterOnchange, name='twitter-onchange/'),

    # other functions
    url(r'^get-total-summary$', views.getTotalSummary, name='get-total-summary/'),


]
