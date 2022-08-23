from django.shortcuts import render, redirect
from .models import Visitante
from .forms import VisitanteForm

def index(request):
    visitante = Visitante.objects.all()
    return render(request, "index.html", {'visitante': visitante})

def cadastro(request):
    form = VisitanteForm()
    if request.method == "POST" or None:
        form = VisitanteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, "cadastro.html", {"form": form})