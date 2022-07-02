from django.shortcuts import redirect, render
from evento_app.forms import EventForm
from evento_app.models import Evento
from django.contrib.auth.decorators import login_required

redirLink = '/evento/'


def home(request):
    data = {}
    data['evt'] = Evento.objects.all()
    return render(request,'event_index.html',data)

@login_required(login_url='account_login')
def form(request):
    data = {}
    data['form'] = EventForm()
    return render(request,'event_form.html',data)

@login_required(login_url='account_login')
def create(request):
    form = EventForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(redirLink)

@login_required(login_url='account_login')
def view(request,pk):
    data = {}
    data['evt'] = Evento.objects.get(pk=pk)
    return render(request, 'event_view.html', data)



@login_required(login_url='account_login')
def edit(request, pk):
    data = {}
    data['evt'] = Evento.objects.get(pk = pk)
    data['form'] = EventForm(instance=data['evt'])
    return render(request,'event_form.html', data)

@login_required(login_url='account_login')
def update(request, pk):
    data = {}
    data['evt'] = Evento.objects.get(pk = pk)
    form = EventForm(request.POST or None, instance=data['evt'])
    if form.is_valid():
        form.save()
        return redirect(redirLink)

@login_required(login_url='account_login')
def delete(request, pk):
    db = Evento.objects.get(pk = pk)
    db.delete()
    return redirect(redirLink)