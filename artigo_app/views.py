from django.shortcuts import redirect, render
from artigo_app.forms import ArtForm
from artigo_app.models import Artigo
from django.contrib.auth.decorators import login_required



@login_required(login_url='account_login')
def home(request):
    data = {}
    data['art'] = Artigo.objects.all()
    return render(request,'art_index.html',data)

@login_required(login_url='account_login')
def form(request):
    data = {}
    data['form'] = ArtForm()
    return render(request,'art_form.html',data)
    

@login_required(login_url='account_login')
def create(request):
    form = ArtForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/artigo/')


@login_required(login_url='account_login')
def view(request,pk):
    data = {}
    data['art'] = Artigo.objects.get(pk=pk)
    return render(request, 'art_view.html', data)
  

@login_required(login_url='account_login')
def edit(request, pk):
    data = {}
    data['art'] = Artigo.objects.get(pk = pk)
    data['form'] = ArtForm(instance=data['art'])
    return render(request,'art_form.html', data)

@login_required(login_url='account_login')
def update(request, pk):
    data = {}
    data['art'] = Artigo.objects.get(pk = pk)
    form = ArtForm(request.POST or None, instance=data['art'])
    if form.is_valid():
        form.save()
        return redirect('/artigo/')
  
@login_required(login_url='account_login')
def delete(request, pk):
    db = Artigo.objects.get(pk = pk)
    db.delete()
    return redirect('/artigo/')