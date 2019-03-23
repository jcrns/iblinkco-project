# importing settings file to access email info
from django.conf import settings

# importing messages from django
from django.contrib import messages

# Importing email functions
from django.core.mail import EmailMessage

# importing django shortcuts and render
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

# importing User Registeraton Form
from .forms import UserRegisterForm

# Importing login_required function from django
from django.contrib.auth.decorators import login_required

# importing firebase
import pyrebase

# Importing pyrebase settings
from .pyrebase_settings import *

# Importing pyrebase settings
from .firebase_auth import *

# importing django auth
from django.contrib import auth


sessionData = []
# Used to connect to firebase server
config = {
    'apiKey': "AIzaSyB-zW5qNKkTlfLzhbigIZkMWypJ4XMAAvY",
    'authDomain': "cpanel-8d88a.firebaseapp.com",
    'databaseURL': "https://cpanel-8d88a.firebaseio.com",
    'projectId': "cpanel-8d88a",
    'storageBucket': "cpanel-8d88a.appspot.com",
    'messagingSenderId': "955905061850"
  }
firebase = pyrebase.initialize_app(config)

authe = firebase.auth()
database = firebase.database()

def signIn(request):
    return render(request, "users/signin.html")

def postSignin(request):
    email = request.POST.get("email")
    passw = request.POST.get("pass")

    # Trying to Sign In
    try:
        user = authe.sign_in_with_email_and_password(email,passw)
        sessionData = {'email':email }
    except Exception as e:
        message = "Invalid Email or Password"

        # Returning Render of page that didn't work
        return HttpResponseRedirect('/signin/')
    # getting User id Token
    session_id = user['idToken']
    print(user)
    request.session['uid'] = str(session_id)

    # Returning Render
    return render(request, "dashboard/home.html", {"email":email})

def logout(request):
    auth.logout(request)
    return render(request, 'users/signin.html')


def signUp(request):

    return render(request, 'users/signup.html')

def postSignUp(request):

    name = request.POST.get('name')
    email = request.POST.get('email')
    passw = request.POST.get('pass')

    try:
        user = authe.create_user_with_email_and_password(email, passw)
    except Exception as e:
        message = "Something Went Wrong"
        return render(request, "users/signup.html", {"messg": message})

    uid = user['localId']
    data = {"name": name, "status": "1 "}
    database.child("users").child(uid).child("details").set(data)

    messages.success(request, f'Congratulations you created an account for iBlinkco! Now Sign In!')

    return render(request, "users/signin.html")

def pyrebaseVerified(function):
    def wrapper(request, *args, **kw):
        session_id = user['idToken']
        if session_id == '':
            return HttpResponseRedirect('/splash/')
        else:
            return function(request, *args, **kw)
    return wrapper

# registering new user
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')

            messages.success(request, f'Congratulations {username} you created an account for iBlinkco!')

            # page that it redirects to
            email = EmailMessage('Welcome to iBlinkco', 'Thank you for signing up to iBlinkco', to=[f'{email}'])
            email.send()
            print({email})
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
