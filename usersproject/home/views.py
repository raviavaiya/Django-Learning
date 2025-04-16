from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate,login


# Create your views here.

def index(request):
    if request.user.is_anonymous:
        # User is authenticated, show the home page or dashboard
        return redirect('/login')
        # User is not authenticated, show the login page or a different page
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')  
        # Handle the login logic here
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            #hgdhs
            login(request, user)
            return render(request, 'index.html')
        else:
            # Handle the case where username is None
            return render(request, 'login.html')
        
    return render(request, 'login.html')

def logoutuser(request):
    logout(request)
    return redirect('/login')
