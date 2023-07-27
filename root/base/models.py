from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
        pass

class certificate_model(models.Model):
        name = models.CharField(max_length=100)
        signed_by = models.CharField(max_length=100)
        certificate_id = models.CharField(max_length=250)



