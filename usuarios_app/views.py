from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib import messages
from django.http import HttpResponse
from .forms import RegisterUserForm
from django.contrib.auth import authenticate,login, logout , update_session_auth_hash
# Create your views here.

def logar_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(request,username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            messages.success(request, 'Usuário logado com sucesso.')
            return redirect('/')
        else:
            messages.error(request, "Username ou senha incorretos! Tente novamente!")
            form_login = AuthenticationForm()
            return redirect('/auth/login/')
    else:
        form_login = AuthenticationForm()
    return render(request, "login.html", {'form_login': form_login})



def cadastrar_user(request):
    if request.method == "POST":
       form_usuario = RegisterUserForm(request.POST)
       if form_usuario.is_valid():
           form_usuario.save()
           username = form_usuario.cleaned_data['username']
           password = form_usuario.cleaned_data['password1']
           user = authenticate(username=username, password=password)
           login(request, user)
           messages.success(request,("Cadastrado com sucesso!"))
           return redirect('/')
    else:
       form_usuario = RegisterUserForm()
    return render(request,'cadastro.html', {'form_usuario': form_usuario})


@login_required(login_url='logar_user')
def deslogar_usuario(request):
    logout(request)
    messages.success(request, 'Usuário deslogado com sucesso.')
    return redirect('/')





    

           