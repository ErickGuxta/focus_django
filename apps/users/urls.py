from django.urls import path
from . import views

urlspatterns = [
    path('',                   views.index,    name = "listar-users"),
    path('criar/',             views.criar,    name = "criar-users"),
    path('<int:id>/detalhar/', views.detalhar, name = "detalhar-users"),
    path('<int:id>/editar/',   views.editar,   name = "editar-users"),
    path('<int:id>/deletar/',  views.deletar,  name = "deletar-users")
]