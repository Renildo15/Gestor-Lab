from django.shortcuts import redirect, render
from projetos_app.forms import ProjectForm
from projetos_app.models import Projeto


def home(request):
    data = {}
    data['pjt'] = Projeto.objects.all()
    return render(request,'project_index.html',data)

def form(request):
    data = {}
    data['form'] = ProjectForm()
    return render(request,'project_form.html',data)


def create(request):
    form = ProjectForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/projeto/')


def view(request,pk):
    data = {}
    data['pjt'] = Projeto.objects.get(pk=pk)
    return render(request, 'project_view.html', data)

def edit(request, pk):
    data = {}
    data['pjt'] = Projeto.objects.get(pk = pk)
    data['form'] = ProjectForm(instance=data['pjt'])
    return render(request,'project_form.html', data)

def update(request, pk):
    data = {}
    data['pjt'] = Projeto.objects.get(pk = pk)
    form = ProjectForm(request.POST or None, instance=data['pjt'])
    if form.is_valid():
        form.save()
        return redirect('/projeto/')

def delete(request, pk):
    db = Projeto.objects.get(pk = pk)
    db.delete()
    return redirect('/projeto/') 