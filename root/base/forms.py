from django.forms import forms, ModelForm
from .models import User


class authform(ModelForm):

    class Meta:
        model = User
        fields = ['email', 'password']