# Create your views here.
from django.shortcuts import render


def produto(request):
    return render(request, 'pagamentos/produto.html')
