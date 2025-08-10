from django.contrib import admin
from django.urls import path, include
from library_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePage.as_view(), name='urlHomePage'),
    path('auth/', AuthPage.as_view(), name='urlAuthPage'),
]
