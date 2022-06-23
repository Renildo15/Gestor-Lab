from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

def pagina_inicial(request):
    return render(request,'PageInicial.html')