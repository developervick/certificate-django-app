from django.shortcuts import render, HttpResponse, redirect
from django.http import request
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .forms import authform, certificate_form, certificate_id_form
from .models import User, certificate_model
from django.db.utils import IntegrityError
import uuid

#!++++++++++++++++++++++++++++++++++++++++---  AUTHENTICATION VIEWS ----++++++++++++++++++++++++++++++++++++++++++++++++++++++
def login_view(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(home)
        else:
            return render(request, 'login.html', {'message':'Invalid user or password'})
    else:
        return render(request, 'login.html')


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
            return render(request, 'signin.html', {'message':"Username already taken"})



    return render(request, 'signin.html')


#!++++++++++++++++++++++++++++++++++++++++---  CERTIFICATE VIEWS ----+++++++++++++++++++++++++++++++++++++++

@login_required
def home(request):
    return render(request, 'index.html')


def certificate(request):

    if request.method == "POST":
        form = certificate_form(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            signed_by = form.cleaned_data['signed_by']
            certificate_id = uuid.uuid4()
            cert = certificate_model(name=name, signed_by=signed_by, certificate_id=certificate_id)
            cert.save()
            return render(request, 'certificate.html', {'message':'certificate Succesfully created',
                                                        'certificate_id':certificate_id})
        else:
            return render(request, 'certificate.html', {'message':'some error occured'})

    return render(request, 'certificate.html')

def validate(request):

    if request.method == 'GET':
        id = request.GET.get('certificate_id', False)
    
    return render(request, 'validate.html', {'message':id})