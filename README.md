<h1 align="center">
    <img width="400px" height="200px" alt="Github" title="Github" src="https://marcas-logos.net/wp-content/uploads/2020/03/GITHUB-LOGO.png?raw=true" />
</h1>

<h3 align="center">
  Django API Test - Sketch made with Django to help me and anyone who wants to.
</h3>

<p align="center">
  <a href="https://github.com/WellingtonFidelis">
    <img alt="By Wellington Fidelis" src="https://img.shields.io/badge/made%20by-Wellington%20Fidelis-5965e0">
  </a>

  <img alt="Last Commit" src="https://img.shields.io/github/last-commit/WellingtonFidelis/django_backend_test?color=rgb(89,101,224)">

  <img alt="Contributors" src="https://img.shields.io/github/contributors/WellingtonFidelis/django_backend_test?color=rgb(89,101,224)">

  <img alt="License" src="https://img.shields.io/badge/license-MIT-%2304D361?color=rgb(89,101,224)">
</p>

<p align="center">
</p>

# :pushpin: Tabela de conteúdos

* [Sobre o projeto](#satisfied-sobre-o-projeto)
* [Layout](#panda_face-layout)
* [Tecnologias](#snowflake-tecnologias)
* [Como rodar o projeto](#question-como-rodar-o-projeto)
* [Autor](#closed_book-autor)

---
# :satisfied: Sobre o projeto
This project was created to use with apps tests, always that need a backend made with Python. This sketch was based at Udemy course and documentation of all frameworks used.

---
# :panda_face: Layout
<!-- * [Figma](https://www.figma.com/file/W9GhJmXJNOZsvA7kcEqOlc/Move.it-1.0-Copy) -->

---
# :snowflake: Tecnologias
* [Python](https://www.python.org)
* [Django](https://www.djangoproject.com)
* [Django Rest Framework](https://www.django-rest-framework.org)
* [Django CORS Headers](https://github.com/adamchainz/django-cors-headers)

---
# :question: Como rodar o projeto
## Acessando direto pelo site:
<!-- * Você pode clicar nesse [link](https://django_backend_test-n0e3rb6sw-wellingtonsilveira.vercel.app/) e acessar a aplicação que está hospedada na plataforma da Vercel. -->

## Rodando na máquina local:
(certifique-se de ter instalado na sua máquina o [Python3](https://www.python.org/downloads/) ou o [Python](https://docs.python.org/2.7/installing/index.html))
1. Abra o terminal na pasta desejada para clonar o repositório e execute o comando:
``` bash
git clone https://github.com/WellingtonFidelis/django_backend_test.git
```
2. Depois de concluído, execute os seguintes comandos:
``` bash
cd django_backend_test
```
3. Para criar um ambiente virtual para melhor desenvolvimento sem afetar a máquina local:
``` bash
python3 -m venv venv
```
4. Após, devemos ativar/ligar esse ambiente:
``` bash
python3 venv/bin/activate
```
5. Instalando as libraries necessárias:
``` bash
pip3 install -r requirements.txt
```
6. Criar as migrations e ativá-las:
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```
7. Rodando o projeto:
```bash
python3 manage.py runserver
```
8. Finalmente para tester, basta abrir o Postman ou Insomnia digitar "http://127.0.0.1:8000/api/form-test/" com o method get. O response deverá ser igual ao exemplo abaixo:
```json
{
  "status": "Ok",
  "message": "Registers called.",
  "result": []
}
```

---
# :closed_book: Autor
Feito por [Wellington Fidelis](https://github.com/WellingtonFidelis).
### :octocat: Github: https://github.com/WellingtonFidelis
### :link: LinkedIn: https://www.linkedin.com/in/wellington-fidelis-7b02b167/
### :camera: Instagram: https://www.instagram.com/wellingtonfidelis/
