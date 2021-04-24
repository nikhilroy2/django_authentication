from django.shortcuts import redirect, render
from .forms import RegisterForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.models import AnonymousUser, User
from django.contrib.auth.decorators import login_required
from .helper import PriceJson
# Create your views here.
def Index(request):
    price_json = PriceJson()
    print(price_json)
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
        messages.info(request, form.error_messages["password_mismatch"])
    form = RegisterForm
    return render(request, 'register.html', {"register": form})




def Login(request):
    #print(request.user)
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
        messages.info(request, form.error_messages["invalid_login"])
        
    form = AuthenticationForm()
    
    if request.user.is_authenticated:
        return redirect('/')
    else:
        return render(request, 'login.html', {"form": form})
        
        


def Logout(request):
    logout(request)
    messages.info(request, f'You have successfully logout')
    return redirect('/')