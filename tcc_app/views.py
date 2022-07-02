from django.shortcuts import redirect, render
from .forms import TccForm
from .models import Tcc
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_safe, require_http_methods

redirLink = '/tcc/'

@require_safe
def home(request):
    data = {}
    data['db'] = Tcc.objects.all()
    return render(request,'tcc_index.html',data)

@require_safe
@login_required(login_url='logar_user')
def form(request):
    data = {}
    data['form'] = TccForm()
    return render(request,'tcc_form.html',data)

@require_http_methods(["POST"])
@login_required(login_url='account_login')
def create(request):
    form = TccForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(redirLink)

@require_safe
@login_required(login_url='account_login')
def view(request,pk):
    data = {}
    data['db'] = Tcc.objects.get(pk=pk)
    return render(request, 'tcc_view.html', data)

@require_safe
@login_required(login_url='account_login')
def edit(request, pk):
    data = {}
    data['db'] = Tcc.objects.get(pk = pk)
    data['form'] = TccForm(instance=data['db'])
    return render(request,'tcc_form.html', data)

@require_http_methods(["POST"])
@login_required(login_url='account_login')
def update(request, pk):
    data = {}
    data['db'] = Tcc.objects.get(pk = pk)
    form = TccForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect(redirLink)

@require_safe
@login_required(login_url='account_login')
def delete(request, pk):
    db = Tcc.objects.get(pk = pk)
    db.delete()
    return redirect(redirLink)


# Create your views here.
