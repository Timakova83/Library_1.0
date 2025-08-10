from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User

class HomePage(View):
    def get(self, request):
        return render(request, 'library_app/home.html')
    
class AuthPage(View):
    def get(self, request):
        return render(request, 'library_app/auth.html')