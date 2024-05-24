from django.shortcuts import render, redirect
from django.http import HttpResponse
from users.forms import RegisterForm, LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout


def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, "register.html", context={"regform": form})
    elif request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                messages.error(request, 'Username already exists.')
                return render(request, "register.html", context={"regform": form})
            else:
                user=form.save()
                user.username = user.username.lower()
                user.save()
                messages.success(request, f'{user.username.title()}, you have successfully registered!')
                login(request, user)
                return redirect('/')
        else:
            return render(request, "register.html", context={"regform": form})

def sign_in(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, "login.html", context={"loginform":form})
    elif request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username'].lower()
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user:
                login(request, user)
                messages.success(request, f'{username.title()}, you have successfully logged in!')
                return redirect('/') 
            else:
                messages.error(request, 'Invalid username or password.')
                return render(request, "login.html", context={"loginform":form})
        else:
            messages.error(request, 'Invalid username or password.')
            return render(request, "login.html", context={"loginform":form})

def sign_out(request):
    logout(request)
    return redirect('/')   