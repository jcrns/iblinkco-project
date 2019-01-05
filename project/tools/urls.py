from django.conf.urls import url, include
from . import views

urlpatterns = [
    # Setting name and url for dashboard
    url(r'^$', views.index, name='tools.index'),
    url(r'^schedule/$', views.schedule, name='tools.schedule'),
    url(r'^likefollow/$', views.likefollow, name='tools.likefollow'),
    url(r'^target/$', views.target, name='tools.target'),
]
