from django.shortcuts import redirect, render
from estagio_app.forms import estForm
from django.core.paginator import Paginator
from estagio_app.models import Estagio
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_safe, require_http_methods

redirLink = '/estagio/'

@require_safe
def home(request):
    estagio = Estagio.objects.all()
    usuario_paginator = Paginator(estagio, 3)
    page_num = request.GET.get('page')
    page = usuario_paginator.get_page(page_num)
    return render(request,'est_index.html',{'page' : page})

@require_safe
@login_required(login_url='logar_user')
def form(request):
    data = {}
    data['form'] = estForm()
    return render(request,'est_form.html',data)

@require_http_methods(["POST"])
@login_required(login_url='logar_user')
def create(request):
    form = estForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(redirLink)

@require_safe
@login_required(login_url='logar_user')
def view(request,pk):
    data = {}
    data['est'] = Estagio.objects.get(pk=pk)
    return render(request, 'est_view.html', data)

@require_safe
@login_required(login_url='logar_user')
def edit(request, pk):
    data = {}
    data['est'] = Estagio.objects.get(pk = pk)
    data['form'] = estForm(instance=data['est'])
    return render(request,'est_form.html', data)

@require_http_methods(["POST"])
@login_required(login_url='logar_user')
def update(request, pk):
    data = {}
    data['est'] = Estagio.objects.get(pk = pk)
    form = estForm(request.POST or None, instance=data['est'])
    if form.is_valid():
        form.save()
        return redirect(redirLink)

@require_http_methods(["POST"])
@login_required(login_url='logar_user')
def delete(request, pk):
    db = Estagio.objects.get(pk = pk)
    db.delete()
    return redirect(redirLink)