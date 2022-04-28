# Cookiecutter Molde
## Objetivo
Criar um molde (setup) que facilite a criação de projetos Python.
Com isso é possível criar projetos de forma rápida e padronizada.

Para utilizar o setup montado nesse projeto é necessário instalar
em sua máquina  o `Cookiecutter`.
A instalação pode ser feita pelo seguinte comando:
!!! note "Instalação do Cookiecutter"
  * `pip install cookiecutter`

    Mais informações do Cookiecutter em [cookiecutter.org](https://cookiecutter.readthedocs.io/en/1.7.2/).

O gerenciamento de dependências e pacotes Python desse projeto é feito pelo Poetry.
!!! note "Instalação do Poetry"
  * <a href="https://python-poetry.org/docs/" target="_blank">Instalação Poetry!</a>

!!! note "Como clonar o projeto?"
  * `cookiecutter git@github.com:thalesteo1995/cookiecutter_molde.git` - clona o projeto para máquina local

Ao clonar o projeto para sua máquina você deverá preencher o formulário abaixo:
### Formuláro:
  * **project_name:** nome do projeto que está criando.
  * **project_slug:** nome do projeto com letras minúsculas e separado por hífen.
  Isso é preenchido automaticamente com base no project_name.
  * **author_name:** autor do projeto.
  * **mantainer_name:** mantenedor do projeto.
  * **author_email:** e-mail do autor.
  * **mantainer_email:** e-mail do mantenedore.
  * **description:** descrição básica do projeto.
### Comandos para montar o projeto :smile:

  * `poetry shell` - Cria e ativa ambiente virtual (.venv);
  * `poetry install` - Instala os requisitos básicos do projeto.