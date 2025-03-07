from django import forms
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth import login, authenticate,logout
from adverts.models import Advert
from advertio.settings import MEDIA_URL
def landing_page(request):
    adverts = Advert.objects.all()
    
    context = {
        'adverts':adverts,
        'MEDIA_URL':MEDIA_URL

    }
    return render(request,'accounts/landing_page.html',context)

def user_registration(request):
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password = raw_password)
            login(request, user)
            return redirect('accounts:profile')
    else:
        form = UserRegistrationForm()
    
    context = {'form': form}
    return render(request,'accounts/registration.html', context)
        


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request = request,data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password = password)
            if user is not None:
                login(request,user)
                messages.success(request,f"{username} logged in successfully.")
                return redirect('accounts:profile')
            else:
                messages.error(request,"Wrong credentials , please try again")
    else:
        form = AuthenticationForm()
    context = {'form': form}
    return render(request,'accounts/login.html', context)


def user_logout(request):
    logout(request)
    messages.success(request,f"{request.user.username} logged out")
    return redirect('accounts:profile')


def profile(request):
    check = "works"
    return render(request, 'accounts/profile.html',{'check':check})
