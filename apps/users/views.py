#importando shortcuts para renderização e redirecionamento de URL
from django.shortcuts import render, get_object_or_404, redirect 

#importando User padrão do django; biblioteca de login_required e user_passes_test para acesso restrito a usuários 
from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import UserForm

User = get_user_model()

def is_admin(user):
    return user.is_superuser

#Dashboard
@login_required
def dashboard(request):
    return render(request, "dashboard.html")

#Listar users
@login_required
@user_passes_test(is_admin)
def index(request):

    users = User.objects.all()

    context = {"users": users}

    #retorno a request, o caminho template e o contexto
    return render(request, "pages/users/index.html", context)

#Criar users
@login_required
@user_passes_test(is_admin)
def create(request):
    #instanciando a metaclasse UserForm
    form = UserForm()

    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("list-users")
        # se não for válido renderiza a tela de criar novamente
        else:
            context = {"form": form}
            return render(request, "pages/users/form.html", context)

    context = {"form": form}
    return render(request, "pages/users/form.html", context)

#Detalhar users
@login_required
@user_passes_test(is_admin)
def detail(request, id):
    #retornar user por ID pegando pelo get
    user = get_object_or_404(User, id=id)

    context = {"user": user}

    return render(request, "pages/users/detail.html", context)


#Editar users
@login_required
@user_passes_test(is_admin)
def edit(request, id):

    user = get_object_or_404(User, id=id)
    form = UserForm(instance=user)

    if request.method == "POST":
        #instancia o UserForm, tendo como parametro: request via POST e a instância do user
        form = UserForm(request.POST, instance=user)

        if form.is_valid():
            form.save()
            return redirect("list-users")
        else:
            context = {
                "is_edit": True,
                "form": form
            }
            return render(request, 'pages/users/form.html', context)

    context = {
        "is_edit": True,
        "form": form
    }
    return render(request, 'pages/users/form.html', context)

#Deletar Users
@login_required
@user_passes_test(is_admin)
def delete(request, id):

    user = get_object_or_404(User, id=id)

    if request.method == "POST":
        user.delete()
        return redirect("list-users")
    
    context = {"delete_user": user}
    return render(request, "pages/users/form.html", context)
