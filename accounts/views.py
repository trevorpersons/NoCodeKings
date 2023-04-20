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
