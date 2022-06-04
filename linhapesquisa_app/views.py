from django.shortcuts import render
from django.shortcuts import redirect, render
from linhapesquisa_app.forms import linhaForm
from linhapesquisa_app.models import LinhaPesquisa
from django.contrib.auth.decorators import login_required




def home(request):
    data = {}
    data['db'] = LinhaPesquisa.objects.all()
    return render(request,'linha_index.html',data)


def form(request):
    data = {}
    data['form'] = linhaForm()
    return render(request,'linha_form.html',data)


def create(request):
    form = linhaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/linhapesquisa/')


def view(request,pk):
    data = {}
    data['db'] = LinhaPesquisa.objects.get(pk=pk)
    return render(request, 'linha_view.html', data)



def edit(request, pk):
    data = {}
    data['db'] = LinhaPesquisa.objects.get(pk = pk)
    data['form'] = linhaForm(instance=data['db'])
    return render(request,'linha_form.html', data)


def update(request, pk):
    data = {}
    data['db'] = LinhaPesquisa.objects.get(pk = pk)
    form = linhaForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('/linhapesquisa/')


def delete(request, pk):
    db = LinhaPesquisa.objects.get(pk = pk)
    db.delete()
    return redirect('/linhapesquisa/')    