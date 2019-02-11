# generic views
from rest_framework import generics, mixins
from dashboard.models import *
from dashboard.serializer import *

# class that runs rest api for Instagram
class InstagramAPIView(generics.ListAPIView): #detailed view
    pass
    lookup_field = 'pk'
    serializer_class = InstagramSerializer
    # queryset = Instagram.objects.all()

    def get_queryset(self):
        return Instagram.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class InstagramRudView(generics.RetrieveUpdateDestroyAPIView): #detailed view
    pass
    lookup_field = 'pk'
    serializer_class = InstagramSerializer
    # queryset = Instagram.objects.all()

    def get_queryset(self):
        return Instagram.objects.all()
