from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Senha
from .forms import RegistrarForm, SenhaForm

# Registrar um usuário
def registrar(request):
    if request.user.is_anonymous:
        if request.method == "POST":
            form = RegistrarForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Conta criada com sucesso.')
                return redirect('/login')
        else:
            form = RegistrarForm()
        context = {"form":form}
        return render(request, 'registration/registrar.html', context)
    else:
        return redirect('/painel')

# Painel principal
@login_required(login_url='/login')
def painel(request):
    # Filtrar as senhas por id do usuário
    usuario_id = request.user.id
    senhas = Senha.objects.filter(usuario=usuario_id)
    # Carregar o formulário para o modal
    form = SenhaForm()
    context = {"form":form, "senhas":senhas}
    return render(request, 'main/painel.html', context)

# Adicionar senhas (Modal)
@login_required(login_url='/login')
def add_senha(request):
    if request.method == "POST":
        form = SenhaForm(request.POST)
        if form.is_valid():
            nova_senha = form.save(commit=False)
            nova_senha.usuario = request.user
            nova_senha.save()
            messages.success(request, 'Senha adicionada com sucesso.')
            return redirect('/painel')
    return redirect('/painel')
    
# Editar senhas (Modal)
@login_required(login_url='/login')
def edit_senha(request, id):
    senha = get_object_or_404(Senha, pk=id)
    if request.user.id == senha.usuario_id:
        form = SenhaForm(request.POST or None, instance=senha)
        if form.is_valid():
            form.save()
            messages.success(request, 'Senha editada com sucesso.')
            return redirect('/painel')
        else:
            messages.error(request, 'Algo deu errado, tente novamente.')
    else:
        messages.error(request, 'Você não tem permissão para editar essa senha.')
        return redirect('/painel')
    context = {"form":form, "senha":senha}
    return render(request, 'main/edit-senha.html', context)


# Deletar senhas (Modal)
@login_required(login_url='/login')
def delete_senha(request, id):
    senha = Senha.objects.get(pk=id)
    if request.user.id == senha.usuario_id:
        senha.delete()
        messages.success(request, 'Senha deletada com sucesso.')
        return redirect('/painel')
    else:
        messages.error(request, 'Você não tem permissão para deletar essa senha.')
        return redirect('/painel')

