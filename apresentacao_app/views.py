from django.shortcuts import redirect, render
from .forms import ApresentacaoForm
from .models import Apresentacao
from django.contrib.auth.decorators import login_required

redirLink = '/apresentacao/'

def home(request):
    data = {}
    data['db'] = Apresentacao.objects.all()
    return render(request,'apresentacao_index.html',data)

@login_required(login_url='account_login')
def form(request):
    data = {}
    data['form'] = ApresentacaoForm()
    return render(request,'apresentacao_form.html',data)

@login_required(login_url='account_login')
def create(request):
    form = ApresentacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(redirLink)

@login_required(login_url='account_login')
def view(request,pk):
    data = {}
    data['db'] = Apresentacao.objects.get(pk=pk)
    return render(request, 'apresentacao_view.html', data)


@login_required(login_url='account_login')
def edit(request, pk):
    data = {}
    data['db'] = Apresentacao.objects.get(pk = pk)
    data['form'] = ApresentacaoForm(instance=data['db'])
    return render(request,'apresentacao_form.html', data)

@login_required(login_url='account_login')
def update(request, pk):
    data = {}
    data['db'] = Apresentacao.objects.get(pk = pk)
    form = ApresentacaoForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect(redirLink)
@login_required(login_url='account_login')
def delete(request, pk):
    db = Apresentacao.objects.get(pk = pk)
    db.delete()
    return redirect(redirLink)