from django.shortcuts import redirect, render
from artigo_app.forms import ArtForm
from django.core.paginator import Paginator
from artigo_app.models import Artigo
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_safe, require_http_methods


redirLink = '/artigo/'


@require_safe
def home(request):
    artigo = Artigo.objects.all()
    usuario_paginator = Paginator(artigo, 3)
    page_num = request.GET.get('page')
    page = usuario_paginator.get_page(page_num)
    return render(request,'art_index.html',{'page': page})


@require_safe
@login_required(login_url='logar_user')
def form(request):
    data = {}
    data['form'] = ArtForm()
    return render(request,'art_form.html',data)
    
@require_http_methods(["POST"])
@login_required(login_url='logar_user')
def create(request):
    form = ArtForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(redirLink)

@require_http_methods(["POST"])
@login_required(login_url='logar_user')
def view(request,pk):
    data = {}
    data['art'] = Artigo.objects.get(pk=pk)
    return render(request, 'art_view.html', data)
  

@require_safe
@login_required(login_url='logar_user')
def edit(request, pk):
    data = {}
    data['art'] = Artigo.objects.get(pk = pk)
    data['form'] = ArtForm(instance=data['art'])
    return render(request,'art_form.html', data)

@require_http_methods(["POST"])
@login_required(login_url='logar_user')
def update(request, pk):
    data = {}
    data['art'] = Artigo.objects.get(pk = pk)
    form = ArtForm(request.POST or None, instance=data['art'])
    if form.is_valid():
        form.save()
        return redirect(redirLink)

@require_safe
@login_required(login_url='logar_user')
def delete(request, pk):
    db = Artigo.objects.get(pk = pk)
    db.delete()
    return redirect(redirLink)