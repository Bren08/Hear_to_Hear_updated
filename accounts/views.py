from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from accounts.forms import LoginForm, UserRegistrationForm


def index(request):
    """Gets index.html file"""
    return render(request, 'index.html')

@login_required
def logout(request):
    """Log my user out"""
    auth.logout(request)
    messages.success(request, "You are now logged out!")
    return redirect(reverse('index'))


def login(request):
    """Log my user in"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])
        
    
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have now logged in!")
                return redirect(reverse('index'))
            else:
                login_form.add_error(None, "Username or password is not correct")
    else:
        login_form = LoginForm()
    return render(request, 'login.html', {"login_form": login_form})


def registration(request):
    """The registration page"""

    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You are now registered!")
                return redirect(reverse('index'))
            else:
                messages.error(request, "Unable to register your account at this time")
    else:
        registration_form = UserRegistrationForm()
    return render(request, 'registration.html', {
        "registration_form": registration_form})
    
    