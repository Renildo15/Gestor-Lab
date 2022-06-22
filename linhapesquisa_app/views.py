from django.shortcuts import render
from django.shortcuts import redirect, render
from linhapesquisa_app.forms import LinhaForm
from linhapesquisa_app.models import LinhaPesquisa
from django.contrib.auth.decorators import login_required

redirLink = '/linhapesquisa/'

@login_required(login_url='account_login')
def home(request):
    data = {}
    data['db'] = LinhaPesquisa.objects.all()
    return render(request,'linha_index.html',data)

@login_required(login_url='account_login')
def form(request):
    data = {}
    data['form'] = LinhaForm()
    return render(request,'linha_form.html',data)

@login_required(login_url='account_login')
def create(request):
    form = LinhaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(redirLink)

@login_required(login_url='account_login')
def view(request,pk):
    data = {}
    data['db'] = LinhaPesquisa.objects.get(pk=pk)
    return render(request, 'linha_view.html', data)


@login_required(login_url='account_login')
def edit(request, pk):
    data = {}
    data['db'] = LinhaPesquisa.objects.get(pk = pk)
    data['form'] = LinhaForm(instance=data['db'])
    return render(request,'linha_form.html', data)

@login_required(login_url='account_login')
def update(request, pk):
    data = {}
    data['db'] = LinhaPesquisa.objects.get(pk = pk)
    form = LinhaForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect(redirLink)

@login_required(login_url='account_login')
def delete(pk):
    db = LinhaPesquisa.objects.get(pk = pk)
    db.delete()
    return redirect(redirLink)    