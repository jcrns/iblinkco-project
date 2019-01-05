# importing settings file to access email info
from django.conf import settings

# importing messages from django
from django.contrib import messages

# Importing email functions
from django.core.mail import EmailMessage

# importing django shortcuts and render
from django.shortcuts import render, redirect

# importing User Registeraton Form
from .forms import UserRegisterForm

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


