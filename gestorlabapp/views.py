from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as login_process

def PaginaInicial(request):
    if request.user.is_authenticated:
        return render(request,'PageInicial.html')
    else:
        return render(request, 'usuarios/login_user.html')
