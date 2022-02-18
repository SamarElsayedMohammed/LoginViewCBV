from django.shortcuts import render

from django.contrib.auth.views import LoginView 
from django.contrib.messages.views import SuccessMessageMixin



def home(request):
    return render(request,'home.html')

class AdminLogin(SuccessMessageMixin ,LoginView):
    template_name = 'registration/login.html'
    # success_url = 'home'
    success_message = 'Welcome to Home page'

