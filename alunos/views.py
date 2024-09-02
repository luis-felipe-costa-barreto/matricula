from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.
def index(request):
    context = {
        'alunos': Alunos.objects.all()
    }
    return render(request, 'index.html', context)

def matricula(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AlunoForm()
    context = {
        'form': form
    }
    return render(request, 'matricula.html', context)