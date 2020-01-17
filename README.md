# lindart

Projeto da loja virtual lindart.com.br

Issue #1 --> O diretorio no ambiente de desenvolvimento 
```
- lindart $ pyenv local 3.8.0
- lindart $ pyenv local
  3.8.0
```
- Instalar e ativar pipenv
```
-> lindart $ pip install pipenv
-> lindart $ pipenv shell
```
- Criar o file Pipfile.lock e sincronizar as pendencias
```
-> (lindart) lindart $ pipenv lock --clear
-> (lindart) lindart $ pipenv sync
```

- Via githib --> Menu Actions 
```
-> criado o file .github/wotkflows/pythonapp.yml
```

Issue #3 --> Instalar a lib Django e setup do Projeto

- criado o diretorio exemplo e o projeto django exemplo
```
-> (exemplo) exemplo $ pipenv install django
-> (exemplo) exemplo $ django-admin startproject base .
```
- informar o Pycharm que o diretorio exemplo é a raiz do pacote
```
  (selecione o diretório exemplo)-> Mark Directory as -> Sources Root
```

- Criado file setup.py 
```
-> copiado conteudo do file setup.py-> https://github.com/renzon/django_pagarme
-> adacptado as variaveis para o projeto lindart
   OBS:
   o projeto exemplo precisa usar o pacote original (lindart - que esta definido dentro do file setup.py)
   é possivel instalar as aplicaçoes apartir de um sistema de arquivo local. Portanto podemos instalar dentro 
   desta aplicação python este pacote exemplo, e podemos instalar com opção editavel. Desta forma ele vai fazer
   um link do meu projeto direto com o codigo fonte que esta fora (pacote lindart)
   *********************************************************************************
   exemplo $ pipenv install -e ..
   Installing -e ..…
   ✔ Installation Succeeded 
   Pipfile.lock (9d976d) out of date, updating to (a6086c)…
   Locking [dev-packages] dependencies…
   Locking [packages] dependencies…
   ✔ Success! 
   Updated Pipfile.lock (9d976d)!
   Installing dependencies from Pipfile.lock (9d976d)…
     🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 5/5 — 00:00:02
   To activate this project's virtualenv, run pipenv shell.
   Alternatively, run a command inside the virtualenv with pipenv run.
   exemplo $ pipenv graph
   lindart==0.1
     - django [required: >=2.0, installed: 3.0.2]
       - asgiref [required: ~=3.2, installed: 3.2.3]
       - pytz [required: Any, installed: 2019.3]
       - sqlparse [required: >=0.2.2, installed: 0.3.0]
   ***********************************************************************************
```

- inserido no settings.py (INSTALLED_APPS) -> 'lindart'
- Executado um add configuration -> start local do django

- instalado as libs flake8 e pytest-django no projeto exemplo
``` 
-> pipenv install --dev flake8 pytest-django
```

Issue #5 --> Removido Pipfile e Pifile.lock da raiz do projeto

Issue #7 --> Realizar um pagamento no Pagarme em ambiente de teste'

- alterar o test_fake() que foi criado inicialmente
```
def test_status_code(client):
    resp = client.get(reverse('lindart:pagamento'))
    assert resp.status_code == 200

Quando executado o teste ocorreu a falha -> Skipped: no Django settings

Solução:
o pytest necessita de uma definição de onde encontrat o setting:
- pode ser um file setup.cfg (onde podemos definir varias propriedades para diferentes frameworks)
[pytest]
DJANGO_SETTINGS_MODULE=base.settings.
python_files=test*.py *tests.py

Quando executado o teste ocorreu a falha -> 'lindart' is not a registered namespace

Solução:
Criar uma app pagamento no projeto exemplo.
(exemplo) exemplo $ mng startapp pagamento
exemplo $ tree
.
├── base
│   ├── asgi.py
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-38.pyc
│   │   ├── settings.cpython-38.pyc
│   │   ├── urls.cpython-38.pyc
│   │   └── wsgi.cpython-38.pyc
│   ├── settings.py
│   ├── tests       <-- mover para dentro da api pagamento
│   │   ├── __init__.py
│   │   └── test_pagina_pagamento.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
├── pagamentos
│   ├── admin.py      <-- apagar nao vamos usar no momento
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py    <-- apagar nao vamos usar no momento 
│   ├── tests.py     <-- apagar nao vamos usar no momento 
│   └── views.py
├── Pipfile
└── Pipfile.lock

- mover o diretorio tests para dentro da app pagamentos
- alterar no setting,py INSTALLED_APPS -> 'pagamento'
- alterar no file test_pagina_pagamento -> 'pagamento:produto'

Quando executado o teste ocorreu a falha -> pagamento' is not a registered namespace

Solução:
- Criar uma view produto no file views.py da api pagamento
def produto(request):
    pass

- criar um url (pode copiar do da api base) dentro da api pagamento
from django.urls import path
from pagamentos import views
app_name = 'pagamentos'
urlpatterns = [
    path('produto/', views.produto, name='produto'),

- dentro do file urls.py da api base incluir:
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('pagamentos/', include('pagamentos.urls'))

- inserir na views.py api pagamento
def produto(request):
    return HttpResponse()

Boilerplate completa do Django (ter uma view completa)
- declarar a view
- declarar o URL
- maperar esta URL
```

- Criar uma pagina para poder efetuar um pagamento. Vamos copiar o codigo do site pagarme
  codigo Javascript para abrir o Checkout.
 
 - Criar o teste para verificar o Jscript do checkout. Para isto o framework do Django 
   fornece umas funçoes para utilizarmos. Esta ferramentas do django sao em unittest 
   e nao em pytest.
   Para este teste criar o file django_assertions.py
   ```
   from django.test import TestCase
   _test_case = TestCase()
   assert_contains = _test_case.assertContains
   ```

- teste criado
```
def test_pagarme_javascript(client):
    resp = client.get(reverse('pagamentos:produto'))
    assert_contains(resp, 'script src="https://assets.pagar.me/checkout/1.1.0/checkout.js"')  
```

- apartir deste ponto podemos acessar a pagina no browser: (em branco aparece a pagina)
-> http://localhost:8000/pagamentos/produto
   
- para retornar uma informação na pagina podemos fazer no file views.ps
```
def produto(request):
    return HttpResponse('script src="https://assets.pagar.me/checkout/1.1.0/checkout.js"')
```
- continuando para podermos visualisar uma pagina onde possamos fazer o pagamento,
  alteramos a views.py
```
def produto(request):
    return render(request, 'pagamentos/produto.html')
```

- executando o teste depoia da alteração da views.py
```
-> django.template.exceptions.TemplateDoesNotExist: pagamentos/produto.html

Solução:
- criar um diretorio -> templates/pagamentos
- criar um file -> produto.html e cola o conteudo copiado da pagina do pagarme

:-) - teste passou

-> acessando -> http://localhost:8000/pagamentos/produto

-> aparece o notão Abrir modal de pagamento e precionando o botao podemos 
   informar os dados pessoais e do cartão.

-> alterando no file produtos.html -> paymentMethods: 'credit_card, boleto',
   aparece o notão Abrir modal de pagamento e precionando o botao podemos
   podemos escolher Cartao de Credito ou Boleto Bancario
   Boleto bancario -> transação nao autorizada
   Cartao de Credito -> Ok

OBS: Alterar no file produto.html
-> customerData: 'False'  para customerData: 'true'
-< com False é o proprio usuario que tem que fornecer estes dados.
```
- Para funcionar copiei o conteudo produto.html do 
  -> https://github.com/renzon/django_pagarme

  