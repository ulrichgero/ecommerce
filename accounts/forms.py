from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from django.forms import inlineformset_factory
from django.db import transaction


from .models import MyUser
import logging

class CreateUserForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ['username', 'email', 'password1', 'password2']


