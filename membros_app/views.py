from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Membro
from .forms import MembroForm
from django.views.decorators.http import require_safe, require_http_methods
from django.core.paginator import Paginator

# Create your views here.
@require_safe
def listar_membros(request):
    membros = Membro.objects.all()
    usuario_paginator = Paginator(membros, 3)
    page_num = request.GET.get('page')
    page = usuario_paginator.get_page(page_num)
    return render(request, 'membro_list.html', {'page': page})


@require_http_methods(["GET", "POST"])
@login_required(login_url='logar_user')
def form_membros(request, id = 0):
    if request.method == 'GET':
        if id == 0:
            form  = MembroForm()
        else:
            membro = Membro.objects.get(pk = id)
            form  = MembroForm(instance = membro)
        return render(request, 'membro_form.html', { 'form':form })
    else:
        if id == 0:
            form  = MembroForm(request.POST)
        else:
            membro = Membro.objects.get(pk = id)
            form  = MembroForm(request.POST, instance = membro)
            
        if form.is_valid():
            form.save()
        return redirect('listar_membros')  

@require_http_methods(["POST"])
@login_required(login_url='logar_user')
def excluir_membro(request, id):
    membro = Membro.objects.get(pk = id)
    membro.delete()
    return redirect('listar_membros')

@require_safe
@login_required(login_url='logar_user')
def visualizar_membro(request, id):
    membro = Membro.objects.get(pk = id)
    return render(request, 'membro_view.html', {'membro': membro})