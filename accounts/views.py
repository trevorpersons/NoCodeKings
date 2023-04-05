from django.http import HttpResponse
from django.shortcuts import render
from .models import User

# Create your views here.


def index(request):
    accounts = User.objects.all()
    return render(request, 'accounts/index.html', {'accounts': accounts})


def detail(request, user_id):
    user = User.objects.get(pk=user_id)
    return render(request, 'accounts/detail.html', {'user': user})
