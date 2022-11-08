from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Pessoa
from .forms import PessoaForm
from django.contrib import messages

# Classe listar
@login_required
def clientes_listar(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'pessoa.html', {'r_pessoas': pessoas})

# Classe novo
@login_required
def clientes_novo(request):
    form = PessoaForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('clientes_listar')
    return render(request, 'formulario.html', {'r_form': form})

# Classe atualizar
@login_required
def clientes_atualizar(request, id):
    pessoa = get_object_or_404(Pessoa, pk=id)
    form = PessoaForm(request.POST or None, request.FILES or None, instance=pessoa)

    if form.is_valid():
        form.save()
        return redirect('clientes_listar')

    return render(request, 'formulario.html', {'r_form': form})

# Classe excluir
@login_required
def clientes_excluir(request, id):
    pessoa = get_object_or_404(Pessoa, pk=id)
    form = PessoaForm(request.POST or None, request.FILES or None, instance=pessoa)

    if request.method == 'POST':
        pessoa.delete()
        return redirect('clientes_listar')

    return render(request, 'excluir.html', {'r_form': form, 'r_pessoa': pessoa})