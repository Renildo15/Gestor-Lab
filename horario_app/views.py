from django.shortcuts import redirect, render
from .forms import HorarioForm
from .models import Horario

def home(request):
    data = {}
    data['db'] = Horario.objects.all()
    return render(request,'horario_index.html',data)


def form(request):
    data = {}
    data['form'] = HorarioForm()
    return render(request,'horario_form.html',data)


def create(request):
    form = HorarioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/horario/')

def view(request,pk):
    data = {}
    data['db'] = Horario.objects.get(pk=pk)
    return render(request, 'horario_view.html', data)







# Create your views here.

