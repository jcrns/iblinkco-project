from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

#Taking to home.html which includes all website files
def index(request):
    return render(request, 'homepage/home.html')
