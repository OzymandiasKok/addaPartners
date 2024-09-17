from django.shortcuts import render, redirect
from .models import Cliente, Registro
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'crm/home.html')

@login_required
def cliente_dashboard(request):
    if request.method == 'POST':
        descricao = request.POST['descricao']
        valor = request.POST['valor']
        cliente = request.user.cliente
        Registro.objects.create(cliente=cliente, descricao=descricao, valor=valor)
        return redirect('cliente_dashboard')
    return render(request, 'crm/cliente_dashboard.html')

@login_required
def funcionario_dashboard(request):
    registros = Registro.objects.all()
    return render(request, 'crm/funcionario_dashboard.html', {'registros': registros})
