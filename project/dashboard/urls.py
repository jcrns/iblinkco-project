from django.conf.urls import url, include
from . import views

urlpatterns = [
    # Setting name and url for dashboard
    url(r'^$', views.index, name='dash.index'),
]
