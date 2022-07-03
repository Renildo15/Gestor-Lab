from django.shortcuts import redirect, render
from .forms import ApresentacaoForm
from .models import Apresentacao
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_safe, require_http_methods

redirLink = '/apresentacao/'

@require_safe
def home(request):
    data = {}
    data['db'] = Apresentacao.objects.all()
    return render(request,'apresentacao_index.html',data)

@require_safe
@login_required(login_url='logar_user')
def form(request):
    data = {}
    data['form'] = ApresentacaoForm()
    return render(request,'apresentacao_form.html',data)


@require_http_methods(["POST"])
@login_required(login_url='logar_user')
def create(request):
    form = ApresentacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(redirLink)
    
@require_safe
@login_required(login_url='logar_user')
def view(request,pk):
    data = {}
    data['db'] = Apresentacao.objects.get(pk=pk)
    return render(request, 'apresentacao_view.html', data)

@require_safe
@login_required(login_url='logar_user')
def edit(request, pk):
    data = {}
    data['db'] = Apresentacao.objects.get(pk = pk)
    data['form'] = ApresentacaoForm(instance=data['db'])
    return render(request,'apresentacao_form.html', data)


@require_http_methods(["POST"])
@login_required(login_url='logar_user')
def update(request, pk):
    data = {}
    data['db'] = Apresentacao.objects.get(pk = pk)
    form = ApresentacaoForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect(redirLink)
    
@require_safe    
@login_required(login_url='logar_user')
def delete(request, pk):
    db = Apresentacao.objects.get(pk = pk)
    db.delete()
    return redirect(redirLink)