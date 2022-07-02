from django.shortcuts import render
from django.shortcuts import redirect, render
from linhapesquisa_app.forms import LinhaForm
from linhapesquisa_app.models import LinhaPesquisa
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_safe, require_http_methods

redirLink = '/linhapesquisa/'

@require_safe
def home(request):
    data = {}
    data['db'] = LinhaPesquisa.objects.all()
    return render(request,'linha_index.html',data)

@require_safe
@login_required(login_url='account_login')
def form(request):
    data = {}
    data['form'] = LinhaForm()
    return render(request,'linha_form.html',data)

@require_http_methods(["POST"])
@login_required(login_url='account_login')
def create(request):
    form = LinhaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(redirLink)

@require_safe
@login_required(login_url='account_login')
def view(request,pk):
    data = {}
    data['db'] = LinhaPesquisa.objects.get(pk=pk)
    return render(request, 'linha_view.html', data)

@require_safe
@login_required(login_url='account_login')
def edit(request, pk):
    data = {}
    data['db'] = LinhaPesquisa.objects.get(pk = pk)
    data['form'] = LinhaForm(instance=data['db'])
    return render(request,'linha_form.html', data)

@require_http_methods(["POST"])
@login_required(login_url='account_login')
def update(request, pk):
    data = {}
    data['db'] = LinhaPesquisa.objects.get(pk = pk)
    form = LinhaForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect(redirLink)
    
@require_safe
@login_required(login_url='account_login')
def delete(request, pk):
    db = LinhaPesquisa.objects.get(pk = pk)
    db.delete()
    return redirect(redirLink)    