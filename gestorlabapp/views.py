from django.shortcuts import redirect, render

def PaginaInicial(request):
    return render(request,'PageInicial.html')
