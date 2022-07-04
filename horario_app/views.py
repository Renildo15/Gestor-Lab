from django.shortcuts import redirect, render
from .forms import HorarioForm
from .models import Horario
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_safe, require_http_methods


redirLink = '/horario/'

@require_safe
def home(request):
    horario = Horario.objects.all()
    usuario_paginator = Paginator(horario, 3)
    page_num = request.GET.get('page')
    page = usuario_paginator.get_page(page_num)
    return render(request,'horario_index.html',{'page' : page})

@require_safe
@login_required(login_url='logar_user')
def form(request):
    data = {}
    data['form'] = HorarioForm()
    return render(request,'horario_form.html',data)

@require_http_methods(["POST"])
@login_required(login_url='logar_user')
def create(request):
    form = HorarioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(redirLink)

@require_safe
@login_required(login_url='logar_user')
def view(request,pk):
    data = {}
    data['db'] = Horario.objects.get(pk=pk)
    return render(request, 'horario_view.html', data)

@require_safe
@login_required(login_url='logar_user')
def edit(request, pk):
    data = {}
    data['db'] = Horario.objects.get(pk = pk)
    data['form'] = HorarioForm(instance=data['db'])
    return render(request,'horario_form.html', data)

@require_http_methods(["POST"])
@login_required(login_url='logar_user')
def update(request, pk):
    data = {}
    data['db'] = Horario.objects.get(pk = pk)
    form = HorarioForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect(redirLink)

@require_safe
@login_required(login_url='logar_user')
def delete(request, pk):
    db = Horario.objects.get(pk = pk)
    db.delete()
    return redirect(redirLink)


# Create your views here.

