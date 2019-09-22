from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import LoginForm, UserRegistrationForm


def products(request):
    """Gets products.html file"""
    return render(request, 'products.html')

@login_required
def logout(request):
    """Log my user out"""
    auth.logout(request)
    messages.success(request, "You are now logged out!")
    return redirect(reverse('products'))


def login(request):
    """Log my user in"""
    if request.user.is_authenticated:
        return redirect(reverse('products'))
    if request.method == "POST":
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])
        
    
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "")
                return redirect(reverse('products'))
            else:
                login_form.add_error(None, "Username or password is not correct")
    else:
        login_form = LoginForm()
    return render(request, 'login.html', {"login_form": login_form})


def registration(request):
    """The registration page"""

    if request.user.is_authenticated:
        return redirect(reverse('products'))

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You are now registered!")
                return redirect(reverse('products'))
            else:
                messages.error(request, "Unable to register your account at this time")
    else:
        registration_form = UserRegistrationForm()
    return render(request, 'registration.html', {
        "registration_form": registration_form})


def user_profile(request):
    """User's profile page"""
    user = User.objects.get(email=request.user.email)
    return render(request, 'profile.html', {"profile": user})
    
    