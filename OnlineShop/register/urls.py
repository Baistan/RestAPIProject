from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('create/',AccountRegisterView.as_view(),name='create'),
    path('login/',UserLoginView.as_view(),name='login'),
    path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        activate, name='activate'),
]
