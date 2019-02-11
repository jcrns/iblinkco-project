# Import Rest API class
from .views import InstagramRudView, InstagramAPIView
from django.conf.urls import url, include

urlpatterns = [
    # Setting name and url for dashboard
    url(r'^$', InstagramAPIView.as_view(), name='post-create'),
    url(r'^(?P<pk>\d+)/$', InstagramRudView.as_view(), name='post-rud'),
]
