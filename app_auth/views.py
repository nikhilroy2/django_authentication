from django.shortcuts import redirect, render
from .forms import RegisterForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.
def Index(request):
    return render(request, 'index.html')

def Register(request):
    name_str = ''
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            username = form.cleaned_data.get('username')
            messages.success(request, f'You have successfully registered {username}')
            name_str= username
            return redirect('/')
    form = RegisterForm
    return render(request, 'register.html', {"register": form})



def Login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back {username}')
                return redirect('/')
            messages.info(request, f'Login failed')
    form = AuthenticationForm()
    return render(request, 'login.html', {"form": form})


def Logout(request):
    logout(request)
    messages.info(request, f'You have successfully logout')
    return redirect('/')