from django.http import HttpResponse
from django.shortcuts import redirect, render
from gestorlabapp.forms import LabForm
from gestorlabapp.models import Lab

def home(request):
    data = {}
    data['db'] = Lab.objects.all()
    return render(request,'index.html',data)

def form(request):
    data = {}
    data['form'] = LabForm()
    return render(request,'form.html',data)


def create(request):
    form = LabForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')