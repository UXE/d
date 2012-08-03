# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def home(request):
    """home view
    """

    return render(request, 'home/home.html', {'guest': True})