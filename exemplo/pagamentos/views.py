# Create your views here.
from django.conf import settings
from django.shortcuts import render


def produto(request):
    ctx = {'CHAVE_LINDART_CRIPTOGRAFIA_PUBLICA': settings.CHAVE_LINDART_CRIPTOGRAFIA_PUBLICA}
    return render(request, 'pagamentos/produto.html', ctx)
