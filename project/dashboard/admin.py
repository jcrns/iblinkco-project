from django.contrib import admin
from dashboard.models import *

# Creating a list of models I want to be used by admins
dashboardModels = [Instagram, Twitter, Youtube, PostSocial, LikeOpperation, FollowOpperation]

# Registering dashboardModels
admin.site.register(dashboardModels)
