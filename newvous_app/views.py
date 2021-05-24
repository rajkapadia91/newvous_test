from django.shortcuts import render, redirect, HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect
from .models import *
# Create your views here.


def index(request):
    return render(request, 'home.html')