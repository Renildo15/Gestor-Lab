from django.shortcuts import redirect, render
from projetos_app.forms import ProjectForm
from projetos_app.models import Projeto
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_safe, require_http_methods

redirLink = '/projeto/'

@require_safe
def home(request):
    data = {}
    data['pjt'] = Projeto.objects.all()
    return render(request,'project_index.html',data)

@require_safe
@login_required(login_url='logar_user')
def form(request):
    data = {}
    data['form'] = ProjectForm()
    return render(request,'project_form.html',data)

@require_http_methods(["POST"])
@login_required(login_url='logar_user')
def create(request):
    form = ProjectForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(redirLink)

@require_safe
@login_required(login_url='logar_user')
def view(request,pk):
    data = {}
    data['pjt'] = Projeto.objects.get(pk=pk)
    return render(request, 'project_view.html', data)

@require_safe
@login_required(login_url='logar_user')
def edit(request, pk):
    data = {}
    data['pjt'] = Projeto.objects.get(pk = pk)
    data['form'] = ProjectForm(instance=data['pjt'])
    return render(request,'project_form.html', data)

@require_http_methods(["POST"])
@login_required(login_url='logar_user')
def update(request, pk):
    data = {}
    data['pjt'] = Projeto.objects.get(pk = pk)
    form = ProjectForm(request.POST or None, instance=data['pjt'])
    if form.is_valid():
        form.save()
        return redirect(redirLink)

@require_http_methods(["POST"])
@login_required(login_url='logar_user')
def delete(request, pk):
    db = Projeto.objects.get(pk = pk)
    db.delete()
    return redirect(redirLink) 