# Create your views here.
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.views import generic
import logging
from django.views.generic.base import TemplateView
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CreateUserForm
from django.views.generic import CreateView
from .models import MyUser


def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form' : form }
    return render(request, 'accounts/register.html', context)



def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user )
            return redirect('home')


    context = {}
    return render(request, 'accounts/login.html', context)




