from django.shortcuts import render, HttpResponse, redirect
from django.http import request
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .forms import authform
from .models import User
from django.db.utils import IntegrityError

@login_required
def home(request):
    return render(request, 'index.html')

def login_view(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect(home)
        else:
            return render(request, 'login.html', {'method':request.method,
                                              'user':username,
                                              'pass':password })
    else:
        return render(request, 'login.html', {'method':request.method})


def logout_view(request):
    logout(request)
    return redirect(login_view)

def signin(request):

    if request.method == 'POST':
        username =request.POST['username']
        password=request.POST['password']

        try:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            login(request, user)
            return redirect(home)
        except IntegrityError:
            return render(request, 'signin.html', {'message':"username already exist"})



    return render(request, 'signin.html')

