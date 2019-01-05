# Importing login_required function from django
from django.contrib.auth.decorators import login_required

# importing User Registeraton Form
from django.contrib.auth.forms import UserCreationForm

# importing authenticatation and login functions from django
from django.contrib.auth import authenticate, login

# importing django shortcuts and render
from django.shortcuts import render, redirect

# Importing models from other apps to be accessed tools model

from .models import *

def index(request):
    return render(request, 'tools/home.html')

@login_required
def schedule(request):
    return render(request, 'tools/home_schedule.html')

@login_required
def likefollow(request):
    return render(request, 'tools/home_likefollow.html')

@login_required
def target(request):
    return render(request, 'tools/home_target.html')
