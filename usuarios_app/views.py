from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as login_process, logout as logout_process
# Create your views here.
def cadastro(request):
    if request.method == "POST":
       form_usuario = UserCreationForm(request.POST)
       if form_usuario.is_valid():
           form_usuario.save()
           return redirect('PaginaInicial')
    else:
       form_usuario = UserCreationForm()
    return render(request,'usuarios/cadastro_user.html', {'form_usuario': form_usuario})


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        usuario =authenticate(request, username=username, password=password)

        if usuario is not None:
            login_process(request, usuario)
            return redirect('PaginaInicial')
        else:
            form_login = AuthenticationForm()
    else:
        form_login = AuthenticationForm()
    return render(request, 'usuarios/login_user.html', {'form_login': form_login})

def logout(request):
    logout_process(request)
    return redirect('login')
    

           