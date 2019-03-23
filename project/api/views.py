# generic views
from rest_framework import generics, mixins
from dashboard.models import *
from .serializers import *
from dashboard.permissions import *
from dashboard.views import *
from django.contrib.auth.models import User

# class that runs rest api for Instagram
class UsersAPIView(mixins.CreateModelMixin, generics.ListAPIView): #detailed view
    lookup_field = 'pk'
    serializer_class = UsersSerializer
    # queryset = Instagram.objects.all()

    def get_queryset(self):
        qs = User.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(Username__iexact=query).distinct()
        return qs

    def perform_create(self, serializer):
        serializer.save()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# class that runs rest api for Instagram
class InstagramAPIView(mixins.CreateModelMixin, generics.ListAPIView): #detailed view
    lookup_field = 'pk'
    serializer_class = InstagramSerializer
    # queryset = Instagram.objects.all()

    def get_queryset(self):
        qs = Instagram.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(instagram_username__iexact=query).distinct()
        return qs

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

# class that runs rest api for Twitter
class TwitterAPIView(mixins.CreateModelMixin, generics.ListAPIView): #detailed view
    lookup_field = 'pk'
    serializer_class = TwitterSerializer
    # queryset = Instagram.objects.all()

    def get_queryset(self):
        qs = Twitter.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(twitter_username__iexact=query).distinct()
        return qs

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
