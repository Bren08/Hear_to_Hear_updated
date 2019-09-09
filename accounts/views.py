from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from accounts.forms import LoginForm


def index(request):
    """Gets index.html file"""
    return render(request, 'index.html')

def logout(request):
    """Log my user out"""
    auth.logout(request)
    messages.success(request, "You are now logged out!")
    return redirect(reverse('index'))

def login(request):
    """Log my user in"""
    if request.method == "POST":
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])
        
    
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have now logged in!")
            else:
                login_form.add_error(None, "Username or password is not correct")
    else:
        login_form = LoginForm()
    return render(request, 'login.html', {"login_form": login_form})
