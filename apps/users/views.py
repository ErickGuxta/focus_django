from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "dashboard.html")


def criar(request):
    return HttpResponse("Criar user")


def detalhar(request, id):
    return HttpResponse(f"Detalhar user {id}")


def editar(request, id):
    return HttpResponse(f"Editar user {id}")


def deletar(request, id):
    return HttpResponse(f"Deletar user {id}")
