from django.urls import path
from . import views

urlpatterns = [
    path('', views.validate, name="validate"),
    path('home', views.home, name='home'),
    path('login', views.login_view, name='login'),
    path('signin', views.signin, name='signin'),
    path('logout', views.logout_view, name='logout'),
    path('certificate', views.certificate, name='certi'),
    path('validate', views.validate, name='validate'),
]