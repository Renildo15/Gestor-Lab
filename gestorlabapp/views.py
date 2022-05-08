from django.http import HttpResponse
from django.shortcuts import render
from gestorlabapp.forms import LabForm

def home(request):
    return render(request,'index.html')

def form(request):
    data = {}
    data['form'] = LabForm()
    return render(request,'form.html',data)