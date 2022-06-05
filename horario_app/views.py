from django.shortcuts import redirect, render
from .forms import HorarioForm
from .models import Horario
from django.contrib.auth.decorators import login_required


@login_required(login_url='account_login')
def home(request):
    data = {}
    data['db'] = Horario.objects.all()
    return render(request,'horario_index.html',data)


@login_required(login_url='account_login')
def form(request):
    data = {}
    data['form'] = HorarioForm()
    return render(request,'horario_form.html',data)


@login_required(login_url='account_login')
def create(request):
    form = HorarioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/horario/')

@login_required(login_url='account_login')
def view(request,pk):
    data = {}
    data['db'] = Horario.objects.get(pk=pk)
    return render(request, 'horario_view.html', data)

@login_required(login_url='account_login')
def edit(request, pk):
    data = {}
    data['db'] = Horario.objects.get(pk = pk)
    data['form'] = HorarioForm(instance=data['db'])
    return render(request,'horario_form.html', data)

@login_required(login_url='account_login')
def update(request, pk):
    data = {}
    data['db'] = Horario.objects.get(pk = pk)
    form = HorarioForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('/horario/')

@login_required(login_url='account_login')
def delete(request, pk):
    db = Horario.objects.get(pk = pk)
    db.delete()
    return redirect('/horario/')


# Create your views here.

