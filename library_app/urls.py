from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePage, name='urlHomePage'),
    path('auth/', AuthPage, name='urlAuthPage'),
]