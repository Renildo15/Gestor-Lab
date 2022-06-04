from django.shortcuts import redirect, render
from projetos_app.forms import ProjectForm
from projetos_app.models import Projeto
from django.contrib.auth.decorators import login_required

@login_required(login_url='account_login')
def home(request):
    data = {}
    data['pjt'] = Projeto.objects.all()
    return render(request,'project_index.html',data)
    
@login_required(login_url='account_login')
def form(request):
    data = {}
    data['form'] = ProjectForm()
    return render(request,'project_form.html',data)

@login_required(login_url='account_login')
def create(request):
    form = ProjectForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/projeto/')

@login_required(login_url='account_login')
def view(request,pk):
    data = {}
    data['pjt'] = Projeto.objects.get(pk=pk)
    return render(request, 'project_view.html', data)

@login_required(login_url='account_login')
def edit(request, pk):
    data = {}
    data['pjt'] = Projeto.objects.get(pk = pk)
    data['form'] = ProjectForm(instance=data['pjt'])

@login_required(login_url='account_login')
def update(request, pk):
    data = {}
    data['pjt'] = Projeto.objects.get(pk = pk)
    form = ProjectForm(request.POST or None, instance=data['pjt'])
    if form.is_valid():
        form.save()
        return redirect('/projeto/')

@login_required(login_url='account_login')
def delete(request, pk):
    db = Projeto.objects.get(pk = pk)
    db.delete()
    return redirect('/projeto/') 