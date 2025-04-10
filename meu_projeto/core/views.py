from django.shortcuts import render
from .models import Materia, Comentario
from .forms import MateriaForm, ComentarioForm
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def index(request):
    # página principal do app core
    return  render(request, 'core/index.html')

@login_required # exige login do usuário para acessar esta aba, no caso as materias
def materias(request):
    # mostra todos os assuntos
    materias = Materia.objects.filter(dono=request.user).order_by('date_added')
    context = {'materias': materias}
    return render(request, 'core/materias.html', context)

@login_required # exige login do usuário para acessar esta aba, no caso as materias
def materia(request, materia_id):
    # mostra uma única materia
    materia = Materia.objects.get(id = materia_id)

    # garante que a matéria pertença ao usuário atual
    if materia.dono != request.user:
        return render(request, 'core/erro_404.html', status=404)
    
    comentarios = materia.comentario_set.order_by('-date_added') # o "-" é para começar da ordem inversa
    context = {'materia': materia, 'comentarios': comentarios}
    return render(request, 'core/materia.html', context)

@login_required # exige login do usuário para acessar esta aba, no caso as materias
def nova_materia(request):
    # Adiciona uma nova matéria
    if request.method != 'POST': # "!=" é diferente
        # Nenhuma materia submetida; cria um formulário em branco
        form = MateriaForm()
    else:
        # Dados de POST submetidos; processa os dados
        form = MateriaForm(request.POST)
        if form.is_valid():
            nova_materia = form.save(commit=False)
            nova_materia.dono = request.user
            nova_materia.save()
            return HttpResponseRedirect(reverse('materias'))
        
    context = {'form': form}
    return render(request, 'core/nova_materia.html', context)

@login_required # exige login do usuário para acessar esta aba, no caso as materias
def novo_comentario(request, materia_id):
    # Acrescenta uma nova entrada para o comentario em particular
    materia = Materia.objects.get(id=materia_id)

        # garante que a matéria pertença ao usuário atual; criar a página de erro 404 personalizada e anexar aqui return HttpResponseRedirect(reverse('erro_404')
    if materia.dono != request.user:
        return render(request, 'core/erro_404.html', status=404)

    if request.method != 'POST':
        # Nenhum comentário submetido; cria um formulário em branco
        form = ComentarioForm()
    else:
        # Dados de POST submetidos; processa os dados
        form = ComentarioForm(data=request.POST)
        if form.is_valid():
            novo_comentario = form.save(commit=False)
            novo_comentario.materia = materia
            novo_comentario.save()
            return HttpResponseRedirect(reverse('materia', args=[materia_id]))
        
    context = {'materia':materia, 'form':form}
    return render(request, 'core/novo_comentario.html', context)

@login_required # exige login do usuário para acessar esta aba, no caso as materias
def editar_comentario(request, comentario_id):
    # Edita um comentario existente
    comentario = Comentario.objects.get(id=comentario_id)
    materia = comentario.materia

    # garante que a matéria pertença ao usuário atual
    if materia.dono != request.user:
        return render(request, 'core/erro_404.html', status=404)
    
    if request.method != 'POST':
        # Requisição inicial; preenche previamente o formulario com a entrada atual
        form = ComentarioForm(instance=comentario)

    else:
        # Dados de POST submetidos; processa os dados
        form = ComentarioForm(instance=comentario, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('materia', args=[materia.id]))
        
    context = {'comentario': comentario, 'materia': materia, 'form': form}

    return render(request, 'core/editar_comentario.html', context)

@login_required
def excluir_materia(request, materia_id):
    materia = Materia.objects.get(id=materia_id)

    if materia.dono != request.user:
        return render(request, 'core/erro_404.html', status=404)
    
    if request.method == 'POST':
        materia.delete()
        return  HttpResponseRedirect(reverse('materias'))
    
    context =  {'materia': materia}
    return render (request, 'core/excluir_materia.html', context)

@login_required
def excluir_comentario(request, comentario_id):
    comentario = Comentario.objects.get(id=comentario_id)
    materia = comentario.materia

    if materia.dono != request.user:
        return render(request, 'core/erro_404.html', status=404)
    
    if request.method == 'POST':
        comentario.delete()
        return HttpResponseRedirect(reverse('materia', args=[materia.id]))
    
    context =  {'comentario': comentario, 'materia': materia}
    return render (request, 'core/excluir_comentario.html', context)

def erro_404(request, exception):
    """View personalizada para erros 404."""
    return render(request, 'core/erro_404.html', status=404)