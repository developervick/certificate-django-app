from django.shortcuts import render, HttpResponse, redirect
from django.http import request



def home(request):
    return render(request, 'index.html')

def login(request):

    return render(request, 'login.html', {'method':request.method})

