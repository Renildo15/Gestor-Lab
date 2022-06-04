from django.shortcuts import redirect, render
from .forms import LabForm
from .models import Lab
from django.contrib.auth.decorators import login_required


@login_required(login_url="/auth/login")
def home(request):
    data = {}
    data['db'] = Lab.objects.all()
    return render(request,'index.html',data)

@login_required(login_url="/auth/login")
def form(request):
    data = {}
    data['form'] = LabForm()
    return render(request,'form.html',data)

@login_required(login_url="/auth/login")
def create(request):
    form = LabForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/laboratorio/')

@login_required(login_url="/auth/login")
def view(request,pk):
    data = {}
    data['db'] = Lab.objects.get(pk=pk)
    return render(request, 'view.html', data)

@login_required(login_url="/auth/login")
def edit(request, pk):
    data = {}
    data['db'] = Lab.objects.get(pk = pk)
    data['form'] = LabForm(instance=data['db'])
    return render(request,'form.html', data)

@login_required(login_url="/auth/login")
def update(request, pk):
    data = {}
    data['db'] = Lab.objects.get(pk = pk)
    form = LabForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('/laboratorio/')

@login_required(login_url="/auth/login")
def delete(request, pk):
    db = Lab.objects.get(pk = pk)
    db.delete()
    return redirect('/laboratorio/')
