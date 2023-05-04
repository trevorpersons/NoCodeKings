from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.shortcuts import render
from . import forms
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import User

# Create your views here.


def index(request):
    accounts = User.objects.all()
    return render(request, 'accounts/index.html', {'accounts': accounts})


def detail(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'accounts/detail.html', {'user': user})


def logout_user(request):
    logout(request)
    return redirect('login')


def login_page(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('home')
        message = 'Login failed!'
    return render(
        request, 'login.html', context={'form': form, 'message': message})
