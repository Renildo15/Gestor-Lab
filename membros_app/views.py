from django.shortcuts import render, redirect
from .models import Membro

# Create your views here.

def listar_membros(request):
    membros = Membro.objects.all()
    
    return render(request, 'list.html', {'membros': membros})