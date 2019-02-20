# generic views
from rest_framework import generics, mixins
from dashboard.models import *
from dashboard.serializers import *
from dashboard.permissions import *
# class that runs rest api for Instagram
class InstagramAPIView(mixins.CreateModelMixin, generics.ListAPIView): #detailed view
    pass
    lookup_field = 'pk'
    serializer_class = InstagramSerializer
    permissions_classes = [IsAdminUser]
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


class InstagramRudView(generics.RetrieveUpdateDestroyAPIView): #detailed view
    lookup_field = 'pk'
    serializer_class = InstagramSerializer
    # queryset = Instagram.objects.all()

    def get_queryset(self):
        return Instagram.objects.all()
