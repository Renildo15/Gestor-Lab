from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from .forms import LabForm
from .models import Lab
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_safe, require_http_methods


redirLink = '/laboratorio/'
formHtml = 'form.html'

@require_safe
def home(request):
    search = request.GET.get('search')

    if search:
        laboratorios = Lab.objects.filter(nome__icontains= search)
        usuario_paginator = Paginator(laboratorios, 3)
        page_num = request.GET.get('page')
        page = usuario_paginator.get_page(page_num)

    else:
        laboratorios = Lab.objects.all()
        usuario_paginator = Paginator(laboratorios, 3)
        page_num = request.GET.get('page')
        page = usuario_paginator.get_page(page_num)
    return render(request,'index.html',{'page': page, 'search': search})

@require_safe
@login_required(login_url='logar_user')
def form(request):
    data = {}
    data['form'] = LabForm()
    return render(request,formHtml,data)

@require_http_methods(["POST"])
@login_required(login_url='logar_user')
def create(request):
    form = LabForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect(redirLink)
    
    return render(request, formHtml, { 'form': form, 'error': True})
        
@require_safe
@login_required(login_url='logar_user')
def view(request,pk):
    data = {}
    data['db'] = Lab.objects.get(pk=pk)
    return render(request, 'view.html', data)

@require_safe
@login_required(login_url='logar_user')
def edit(request, pk):
    data = {}
    data['db'] = Lab.objects.get(pk = pk)
    data['form'] = LabForm(instance=data['db'])
    return render(request,formHtml, data)

@require_http_methods(["POST"])
@login_required(login_url='logar_user')
def update(request, pk):
    data = {}
    data['db'] = Lab.objects.get(pk = pk)
    form = LabForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect(redirLink)

@require_safe
@login_required(login_url='logar_user')
def delete(request, pk):
    db = Lab.objects.get(pk = pk)
    db.delete()
    return redirect(redirLink)
