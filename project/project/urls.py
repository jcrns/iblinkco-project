"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib.auth import views as auth_views
from users import views as user_views
from dashboard import views

# Main url page and includes all views files
urlpatterns = [

    # Regular app urls
    url(r'^admin/', admin.site.urls),
    url(r'^', include('homepage.urls')),
    url(r'^dashboard/', include('dashboard.urls')),
    url(r'^dashboard-get/', views.InstagramList.as_view()),

    # Rest API URL
    url(r'^api/', include('api.urls')),

    # Login and Registration system urls
    url(r'^register/', user_views.register, name='register'),
    url(r'^login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    url(r'^logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

    # Password Reset urls
    url(r'^password-reset/',
        auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),
        name='password_reset'),

    url(r'^password-reset/done/',
        auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
        name='password_reset_done'),

    url(r'^password-reset-confirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
        name='password_reset_confirm'),

    # Firebase Testing
    url(r'^signin/', user_views.signIn, name='signin'),
    url(r'^postsignin/', user_views.postSignin),
    url(r'^logout-test/', user_views.logout, name='log'),
    url(r'^signup/', user_views.signUp, name='signup'),
    url(r'^postsignup/', user_views.postSignUp, name='postsignup'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
