from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as login_process
# Create your views here.
def cadastro(request):
    if request.method == "GET":
        return render(request,'usuarios/cadastro_user.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse('Ja exixte um usuario com esse username')
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()
        return HttpResponse('Usuario cadastrado com sucesso')

def login(request):

    if request.method == "GET":
        return render(request, 'usuarios/login_user.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        user = authenticate(username=username, password=senha)

        if user is not None:
            login_process(request, user)
            return redirect('PaginaInicial')
        else:
            return HttpResponse('algo invalido')