from django import contrib
from django.conf.urls import url, include
from frontend.views import home, register, profile

urlpatterns = [
    url('accounts/', include('django.contrib.auth.urls')),
    url('home/', home, name='home'),
    url('register/', register, name='register'),
    url('profile/', profile, name='profile'),
]