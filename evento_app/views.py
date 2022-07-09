from django.shortcuts import redirect, render
from evento_app.forms import EventForm
from django.core.paginator import Paginator
from evento_app.models import Evento
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_safe, require_http_methods

redirLink = '/evento/'

@require_safe
def home(request):

    search = request.GET.get('search')

    if search:
        evento = Evento.objects.filter(titulo__icontains=search)
        usuario_paginator = Paginator(evento, 3)
        page_num = request.GET.get('page')
        page = usuario_paginator.get_page(page_num)
    else:
        evento = Evento.objects.all()
        usuario_paginator = Paginator(evento, 3)
        page_num = request.GET.get('page')
        page = usuario_paginator.get_page(page_num)
    return render(request,'event_index.html',{'page' : page})

@require_safe
@login_required(login_url='logar_user')
def form(request):
    data = {}
    data['form'] = EventForm()
    return render(request,'event_form.html',data)

@require_http_methods(["POST"])
@login_required(login_url='logar_user')
def create(request):
    form = EventForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(redirLink)

@require_safe
@login_required(login_url='logar_user')
def view(request,pk):
    data = {}
    data['evt'] = Evento.objects.get(pk=pk)
    return render(request, 'event_view.html', data)

@require_safe
@login_required(login_url='logar_user')
def edit(request, pk):
    data = {}
    data['evt'] = Evento.objects.get(pk = pk)
    data['form'] = EventForm(instance=data['evt'])
    return render(request,'event_form.html', data)

@require_http_methods(["POST"])
@login_required(login_url='logar_user')
def update(request, pk):
    data = {}
    data['evt'] = Evento.objects.get(pk = pk)
    form = EventForm(request.POST or None, instance=data['evt'])
    if form.is_valid():
        form.save()
        return redirect(redirLink)

@require_http_methods(["POST"])
@login_required(login_url='logar_user')
def delete(request, pk):
    db = Evento.objects.get(pk = pk)
    db.delete()
    return redirect(redirLink)