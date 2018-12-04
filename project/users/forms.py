from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# User Registration Form
class UserRegisterForm(UserCreationForm):

    # creating custom form by importing UserRegisterForm and adding custom fields
    email = forms.EmailField()

    class Meta:
        model = User
        # Fields user needs to sign up
        fields = ['username', 'email', 'password1', 'password2']
