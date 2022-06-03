from django.shortcuts import redirect, render
from artigo_app.forms import ArtForm
from artigo_app.models import Artigo


def home(request):
    if request.user.is_authenticated:
        data = {}
        data['art'] = Artigo.objects.all()
        return render(request,'art_index.html',data)
    else:
        return render(request, 'usuarios/login_user.html')
def form(request):
    if request.user.is_authenticated:
        data = {}
        data['form'] = ArtForm()
        return render(request,'art_form.html',data)
    else:
        return render(request, 'usuarios/login_user.html')


def create(request):
    if request.user.is_authenticated:
        form = ArtForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('/artigo/')
    else:
        return render(request, 'usuarios/login_user.html')



def view(request,pk):
    if request.user.is_authenticated:
        data = {}
        data['art'] = Artigo.objects.get(pk=pk)
        return render(request, 'art_view.html', data)
    else:
        return render(request, 'usuarios/login_user.html')


def edit(request, pk):
    if request.user.is_authenticated:
        data = {}
        data['art'] = Artigo.objects.get(pk = pk)
        data['form'] = ArtForm(instance=data['art'])
        return render(request,'art_form.html', data)
    else:
        return render(request, 'usuarios/login_user.html')

def update(request, pk):
    if request.user.is_authenticated:
        data = {}
        data['art'] = Artigo.objects.get(pk = pk)
        form = ArtForm(request.POST or None, instance=data['art'])
        if form.is_valid():
            form.save()
            return redirect('/artigo/')
    else:
        return render(request, 'usuarios/login_user.html')

def delete(request, pk):
    if request.user.is_authenticated:
        db = Artigo.objects.get(pk = pk)
        db.delete()
        return redirect('/artigo/')
    else:
        return render(request, 'usuarios/login_user.html')