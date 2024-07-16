from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from .models import Pessoa

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')  # Redirecione para a página principal após o login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def criar_predio(request):
    nome_predio = None
    if request.method == 'POST':
        nome_predio = request.POST.get('nome_predio')
        if nome_predio:
            # Cria um grupo para o novo prédio
            grupo, created = Group.objects.get_or_create(name=nome_predio)
    return render(request, 'criarpredio.html', {'nome_predio': nome_predio})

def first(request):
    return render(request, 'first.html')

@login_required
def logoff(request):
    auth_views.LogoutView.as_view()
    return redirect(first)

@login_required
def home(request):
    return render(request, 'home.html')

def some_view(request):
    # Assuming you have logic to get the current user or relevant person
    current_user = request.user
    pessoa = Pessoa.objects.filter(user=current_user).first()

    context = {
        'is_sindico': pessoa.sindico if pessoa else False,
    }

    return render(request, 'your_template.html', context)