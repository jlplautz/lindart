# lindart
Projeto da loja virtual Lindart.com.br

O diretorio no ambiente de desenvolvimento esta com Python 3.8.0
- lindart $ pyenv local 3.8.0
- lindart $ pyenv local
  3.8.0
- Instalar pipenv => lindart $ pip install pipenv
- ativar pipenv   => lindart $ pipenv shell
- Criar o file Pipfile.lock => (lindart) lindart $ pipenv lock --clear
- Atualizar as depedencias apartir do Pipfile.lock => (lindart) lindart $ pipenv sync

Via githib --> Actions foi criado o file .github/wotkflows/pythonapp.yml

Issue #3 --> Instalar a lib Django e detup do Projeto
- criado o diretorio exemplo
- instalado a lib django no diretorio exemplo
- criado projeto django -> (exemplo) exemplo $ django-admin startproject base .
- informar o Pycharm que o diretorio exemplo é a raiz do pacote
  exemplo -> Mark Directory as -> Sources Root
- Criado file setup.py -> copiado conteudo do -> https://github.com/renzon/django_pagarme

- OBS:
- o projeto exemplo precisa usar o pacote original (lindart - que esta definido dentro do file setup.py)
  é possivel instalar as aplicaçoes apartir de um sistema de arquivo local. Portanto podemos instalar dentro 
  desta aplicação python este pacote exemplo, e podemos instalar com opção editavel. Desta forma ele vai fazer
  um link do meu projeto direto com o codigo fonte que esta fora (pacote lindart)
************************************************************************************************************
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
************************************************************************************************************

- inserido no settings.py (INSTALLED_APPS) -> 'lindart'
- Executado um add configuration -> start local do django
- pipenv install --dev flake8 -> projeto exemplo
- pipenv install --dev pytest-django -> projeto exemplo