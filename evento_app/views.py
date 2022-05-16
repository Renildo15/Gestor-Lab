from django.shortcuts import redirect, render
from evento_app.forms import EventForm
from evento_app.models import Evento


def home(request):
    data = {}
    data['evt'] = Evento.objects.all()
    return render(request,'event_index.html',data)

def form(request):
    data = {}
    data['form'] = EventForm()
    return render(request,'event_form.html',data)


def create(request):
    form = EventForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/evento/')


def view(request,pk):
    data = {}
    data['evt'] = Evento.objects.get(pk=pk)
    return render(request, 'event_view.html', data)

def edit(request, pk):
    data = {}
    data['evt'] = Evento.objects.get(pk = pk)
    data['form'] = EventForm(instance=data['evt'])
    return render(request,'event_form.html', data)

def update(request, pk):
    data = {}
    data['evt'] = Evento.objects.get(pk = pk)
    form = EventForm(request.POST or None, instance=data['evt'])
    if form.is_valid():
        form.save()
        return redirect('/evento/')

def delete(request, pk):
    db = Evento.objects.get(pk = pk)
    db.delete()
    return redirect('/evento/')