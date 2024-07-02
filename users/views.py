from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.

def signup(request):
    
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        if request.POST['password1'] == request.POST['password2']:
            #register user
            try:
                user = User.objects.create_user(username=request.POST['email'],
                password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('homeuser')
            except IntegrityError:
                return render(request, 'signup.html',{
                    "error": 'Email Already Exist'
                })
        return render(request, 'signup.html',{
                    "error": 'Password do not match'
                })

@login_required
def homeuser(request):
    return render(request, 'homeuser.html')

@user_passes_test(lambda u: u.is_superuser, login_url='/permission-denied/')
def homeadmin(request):
    return render(request, 'homeadmin.html')

def permissiondenied(request):
    return render(request, 'permissiondenied.html')

def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'GET':
        return render(request,'signin.html')
    else:
        user = authenticate(
            request, username=request.POST['email'], password=request.POST
            ['password'])
        if user is None:
            return render(request,'signin.html',{
                'error': 'Username or Password is Incorrect'
            })
        else:
            login(request, user)
            return redirect('homeuser')