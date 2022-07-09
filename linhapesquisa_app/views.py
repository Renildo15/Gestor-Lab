from django.shortcuts import render
from django.shortcuts import redirect, render
from linhapesquisa_app.forms import LinhaForm
from django.core.paginator import Paginator
from linhapesquisa_app.models import LinhaPesquisa
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_safe, require_http_methods

redirLink = '/linhapesquisa/'

@require_safe
def home(request):

    search = request.GET.get('search')
    if search:
        linha = LinhaPesquisa.objects.filter(nome__icontains =  search)
        usuario_paginator = Paginator(linha, 3)
        page_num = request.GET.get('page')
        page = usuario_paginator.get_page(page_num)
    else:
        linha = LinhaPesquisa.objects.all()
        usuario_paginator = Paginator(linha, 3)
        page_num = request.GET.get('page')
        page = usuario_paginator.get_page(page_num)
    return render(request,'linha_index.html',{'page': page})

@require_safe
@login_required(login_url='logar_user')
def form(request):
    data = {}
    data['form'] = LinhaForm()
    return render(request,'linha_form.html',data)

@require_http_methods(["POST"])
@login_required(login_url='logar_user')
def create(request):
    form = LinhaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(redirLink)

@require_safe
@login_required(login_url='logar_user')
def view(request,pk):
    data = {}
    data['db'] = LinhaPesquisa.objects.get(pk=pk)
    return render(request, 'linha_view.html', data)

@require_safe
@login_required(login_url='logar_user')
def edit(request, pk):
    data = {}
    data['db'] = LinhaPesquisa.objects.get(pk = pk)
    data['form'] = LinhaForm(instance=data['db'])
    return render(request,'linha_form.html', data)

@require_http_methods(["POST"])
@login_required(login_url='logar_user')
def update(request, pk):
    data = {}
    data['db'] = LinhaPesquisa.objects.get(pk = pk)
    form = LinhaForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect(redirLink)
    
@require_safe
@login_required(login_url='logar_user')
def delete(request, pk):
    db = LinhaPesquisa.objects.get(pk = pk)
    db.delete()
    return redirect(redirLink)    