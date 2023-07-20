from django.shortcuts import render, HttpResponse
from django.http import request


def home (request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')
