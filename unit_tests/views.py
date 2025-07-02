from django.shortcuts import render, HttpResponse, redirect
from .forms import RegistrationForm, LoginForm
from . import templates
from django.contrib.auth import login, authenticate, logout

# Create your views here.
def home(request) -> HttpResponse:
    return HttpResponse('<h1>Hello world!</h1>')


def register(request) -> render:
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form':form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def log_out(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('home')