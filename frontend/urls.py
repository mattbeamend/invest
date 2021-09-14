from django import contrib
from django.conf.urls import url, include
from frontend.views import dashboard, landing, register

urlpatterns = [
    url('accounts/', include('django.contrib.auth.urls')),
    url('dashboard/', dashboard, name='dashboard'),
    url('register/', register, name='register'),
    url('', landing, name='landing'),
]