# importing User Registeraton Form
from django.contrib.auth.forms import UserCreationForm

# importing authenticatation and login functions from django
from django.contrib.auth import authenticate, login

# importing django shortcuts and render
from django.shortcuts import render, redirect

#Taking to home.html which includes all website files
def index(request):
    return render(request, 'homepage/home.html')
