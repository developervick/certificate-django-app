from django.forms import forms, ModelForm
from django import forms
from .models import User, certificate_model


class authform(ModelForm):

    class Meta:
        model = User
        fields = ['email', 'password']

class certificate_form(ModelForm):

    class Meta:
        model = certificate_model
        fields = ['name', 'signed_by']
