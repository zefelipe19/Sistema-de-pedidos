from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse

# Local imports
from .forms import NewUserForm


class SignUp(View):
    def get(self, request):
        form = NewUserForm
        context = {
            'form': NewUserForm,
        }
        return render(request, 'signup.html', context)


class Login(View):
    def get(self, request):
        return HttpResponse("login")


def logout(request):
    return HttpResponse('logout')
