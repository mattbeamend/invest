from django import contrib
from django.conf.urls import url, include
from frontend.views import home, register, settings

urlpatterns = [
    url('accounts/', include('django.contrib.auth.urls')),
    url('home/', home, name='home'),
    url('settings/', settings, name='settings'),
    url('register/', register, name='register'),
]