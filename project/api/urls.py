# Import Rest API class
from .views import *
from django.conf.urls import url, include

urlpatterns = [
    # Setting name and url for dashboard
    url(r'^users', UsersAPIView.as_view(), name='users-api'),
    url(r'^instagram', InstagramAPIView.as_view(), name='instagram-api'),
    url(r'^twitter', TwitterAPIView.as_view(), name='twitter-api'),
    # url(r'^users', UsersAPIView.as_view(), name='post-create'),
    # url(r'^(?P<pk>\d+)/$', InstagramRudView.as_view(), name='post-rud'),
]
