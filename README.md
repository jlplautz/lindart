<h3># LINDART</h3>

<b>Projeto da loja virtual lindart.com.br</b>


[![codecov](https://codecov.io/gh/jlplautz/lindart/branch/master/graph/badge.svg)](https://codecov.io/gh/jlplautz/lindart)


Issue #1 - <b>O diretório no ambiente de desenvolvimento</b> 
```
- lindart $ pyenv local 3.8.0
- lindart $ pyenv local
  3.8.0
```
<b>- Instalar e ativar pipenv</b>
```
-> lindart $ pip install pipenv
-> lindart $ pipenv shell
```
<b>- Criar o file Pipfile.lock e sincronizar as dependências</b>
```
-> (lindart) lindart $ pipenv lock --clear
-> (lindart) lindart $ pipenv sync
```

<b>- Via githib --> Menu Actions</b> 
```
-> criado o file .github/wotkflows/pythonapp.yml
```

Issue #3 - <b>Instalar a lib Django e setup do Projeto</b>

<b>- criado o diretório exemplo e o projeto django exemplo</b>
```
-> (exemplo) exemplo $ pipenv install django
-> (exemplo) exemplo $ django-admin startproject base .
```
<b>- informar o Pycharm que o diretório exemplo é a raiz do pacote</b>
```
  (selecione o diretório exemplo)-> Mark Directory as -> Sources Root
```

<b>- Criado file setup.py</b> 
```
-> copiado conteúdo do file setup.py-> https://github.com/renzon/django_pagarme
-> adaptado as variaveis para o projeto lindart
   OBS:
   o projeto exemplo precisa usar o pacote original (lindart - que esta definido dentro do file setup.py)
   é possível instalar as aplicações apartir de um sistema de arquivo local. Portanto podemos instalar dentro 
   desta aplicação python este pacote exemplo, e podemos instalar com opção editável. Desta forma ele vai fazer
   um link do projeto exemplo direto com o codigo fonte que esta fora (pacote lindart)

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
```

<b>- Inserido no settings.py (INSTALLED_APPS) -> 'lindart'</b>
<b>- Executado um add configuration -> start local do django</b>

<b>- Instalado as libs flake8 e pytest-django no projeto exemplo</b>
``` 
-> pipenv install --dev flake8 pytest-django
```

Issue #5 - <b>Removido Pipfile e Pifile.lock da raiz do projeto</b>

Issue #7 - <b>Realizar um pagamento no Pagarme em ambiente de teste'</b>

<b>- alterar o test_fake() que foi criado inicialmente</b>
```
def test_status_code(client):
    resp = client.get(reverse('lindart:pagamento'))
    assert resp.status_code == 200
```
<b>Quando executado o teste ocorreu a falha -> Skipped: no Django settings</b>

<b>Solução:</b>
o pytest necessita de uma definição de onde encontrat o setting:
- pode ser um file setup.cfg (onde podemos definir varias propriedades para diferentes frameworks)
```
[pytest]
DJANGO_SETTINGS_MODULE=base.settings.
python_files=test*.py *tests.py
```
<b>Quando executado o teste ocorreu a falha -> 'lindart' is not a registered namespace</b>

<b>Solução:</b>
Criar uma app pagamento no projeto exemplo.
(exemplo) exemplo $ mng startapp pagamento

<b>exemplo $ tree</b>
```
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
```

<b>- Removido o diretorio tests para dentro da app pagamentos</b>
<b>- Alterado no setting.py INSTALLED_APPS -> 'pagamento'</b>
<b>- Alterado no file test_pagina_pagamento -> 'pagamento:produto'</b>

Quando executado o teste ocorreu a falha -> pagamento' is not a registered namespace/b>

<b>Solução:</b>
- Criar uma view produto no file views.py da api pagamento
```
def produto(request):
    pass
```
<b>- criar um url (pode copiar do da api base) dentro da api pagamento</b>
```
from django.urls import path
from pagamentos import views
app_name = 'pagamentos'
urlpatterns = [
    path('produto/', views.produto, name='produto'),
```
<b>- dentro do file urls.py da api base incluir:</b>
```
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('pagamentos/', include('pagamentos.urls'))
```
<b>- inserir na views.py api pagamento</b>
```
def produto(request):
    return HttpResponse()
```
<b>Boilerplate completa do Django (ter uma view completa)</b>
- declarar a view
- declarar o URL
- maperar esta URL

- Criar uma pagina para poder efetuar um pagamento. Vamos copiar o codigo do site pagarme
  codigo Javascript para abrir o Checkout.
  <a href="https://docs.pagar.me/docs/inserindo-o-checkout">https://docs.pagar.me/docs/inserindo-o-checkout</a>
 
 - Criar o teste para verificar o Jscript do checkout. Para isto o framework do Django 
   fornece umas funçoes para utilizarmos. Esta ferramentas do django sao em unittest 
   e nao em pytest.
   Para este teste criar o file django_assertions.py
   ```
   from django.test import TestCase
   _test_case = TestCase()
   assert_contains = _test_case.assertContains
   ```

<b>- teste criado</b>
```
def test_pagarme_javascript(client):
    resp = client.get(reverse('pagamentos:produto'))
    assert_contains(resp, 'script src="https://assets.pagar.me/checkout/1.1.0/checkout.js"')  
```

<b>- apartir deste ponto podemos acessar a pagina no browser: (em branco aparece a pagina)</b>
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

- executando o teste depois da alteração da views.py

-> django.template.exceptions.TemplateDoesNotExist: pagamentos/produto.html

Solução:
- criar um diretorio -> templates/pagamentos
- criar um file -> produto.html e cola o conteúdo copiado da pagina do pagarme

:-) - teste passou

-> acessando -> http://localhost:8000/pagamentos/produto

-> aparece o notão Abrir modal de pagamento e precionando o botao podemos 
   informar os dados pessoais e do cartão.

-> alterando no file produtos.html -> paymentMethods: 'credit_card, boleto',
   aparece o botão <b>Abrir modal de pagamento</b> e precionando o botao podemos
   podemos escolher <b>Cartao de Credito ou Boleto Bancario</b>
   Boleto bancario -> transação nao autorizada
   Cartao de Credito -> Ok

OBS: Alterar no file produto.html
-> customerData: 'False'  para customerData: 'true'
-< com False é o proprio usuario que tem que fornecer estes dados.

- Para funcionar copiei o conteudo produto.html do 
  -> https://github.com/renzon/django_pagarme

 Issue #9 - <b>Remover flake8 da raiz e corrigi o README</b>
 
 - Conteúdo do flake8 foi incorporado no file setup.cfg
 ```
[flake8]
max-line-length = 120
exclude = .venv
```

- Erros ortogáfricos corrigidos do README e melhorado apresentação.
- Usado recomendação do Raul Esteves -<b>Como fazer um README.md BONITÃO</b>


Issue #11 - <b>Instalar lib Codevcov</b>

- Instalado lib Codecov
```
(exemplo) exemplo $ pipenv install --dev pytest-cov
Courtesy Notice: Pipenv found itself running within a virtual environment, so it will automatically use that environment, 
instead of creating its own for any project. You can set PIPENV_IGNORE_VIRTUALENVS=1 to force pipenv to ignore that 
environment and create its own instead. You can set PIPENV_VERBOSITY=-1 to suppress this warning.
Installing pytest-cov…
✔ Installation Succeeded 
Pipfile.lock (796ba5) out of date, updating to (ceda80)…
Locking [dev-packages] dependencies…
✔ Success! 
Locking [packages] dependencies…
✔ Success! 
Updated Pipfile.lock (796ba5)!
Installing dependencies from Pipfile.lock (796ba5)…
  🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 28/28 — 00:00:07
```

<b>- Inserido no file pythonapp.yml</b>
```
  build:
    env:
      global:
      PIPENV_NO_INIHERIT: 1
      PIPENV_VENV_IN_PROJECT: 1
      PIPENV_IGNORE_VIRTUALENVS: -1
...
    - name: Generate coverage report
      working-directory: ./exemplo
      run: |
        pip install pytest
        pip install pytest-cov
        pipenv run pytest --cov=./lindart

      after_sucess:
        - pipenv run codecov
```