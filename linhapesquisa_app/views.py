from django.shortcuts import render
from django.shortcuts import redirect, render
from linhapesquisa_app.forms import linhaForm
from linhapesquisa_app.models import LinhaPesquisa
from django.contrib.auth.decorators import login_required



@login_required(login_url="/auth/login")
def home(request):
    data = {}
    data['db'] = LinhaPesquisa.objects.all()
    return render(request,'linha_index.html',data)

@login_required(login_url="/auth/login")
def form(request):
    data = {}
    data['form'] = linhaForm()
    return render(request,'linha_form.html',data)

@login_required(login_url="/auth/login")
def create(request):
    form = linhaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/linhapesquisa/')

@login_required(login_url="/auth/login")
def view(request,pk):
    data = {}
    data['db'] = LinhaPesquisa.objects.get(pk=pk)
    return render(request, 'linha_view.html', data)


@login_required(login_url="/auth/login")
def edit(request, pk):
    data = {}
    data['db'] = LinhaPesquisa.objects.get(pk = pk)
    data['form'] = linhaForm(instance=data['db'])
    return render(request,'linha_form.html', data)

@login_required(login_url="/auth/login")
def update(request, pk):
    data = {}
    data['db'] = LinhaPesquisa.objects.get(pk = pk)
    form = linhaForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('/linhapesquisa/')

@login_required(login_url="/auth/login")
def delete(request, pk):
    db = LinhaPesquisa.objects.get(pk = pk)
    db.delete()
    return redirect('/linhapesquisa/')    