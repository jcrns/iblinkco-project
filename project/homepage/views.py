# importing User Registeraton Form
from django.contrib.auth.forms import UserCreationForm

# importing messages from django
from django.contrib import messages

# importing authenticatation and login functions from django
from django.contrib.auth import authenticate, login

# importing django shortcuts and render
from django.shortcuts import render, redirect

# importing contact us form
from homepage.forms import ContactForm

# importing pyrebase(backend)
import pyrebase

#Taking to home.html which includes all website files

#
config = {
    'apiKey': "AIzaSyB-zW5qNKkTlfLzhbigIZkMWypJ4XMAAvY",
    'authDomain': "cpanel-8d88a.firebaseapp.com",
    'databaseURL': "https://cpanel-8d88a.firebaseio.com",
    'projectId': "cpanel-8d88a",
    'storageBucket': "cpanel-8d88a.appspot.com",
    'messagingSenderId': "955905061850"
  }
firebase = pyrebase.initialize_app(config)


def index(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_item = form.save(commit=False)
            contact_item.save()
            messages.success(request, f'Thanks filling out the form we will contact you soon!')
    else:
        form = ContactForm()
    return render(request, 'homepage/home.html',{'form':form})
