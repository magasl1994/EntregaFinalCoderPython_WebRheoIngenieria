from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from AppUsers.forms import UserRegisterForm, UserEditForm

def login_request(request):

    msg_login = ""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user is not None:
                login(request, user)
                return render(request, "AppRheo/postlog.html")

        msg_login = "Usuario o contraseña incorrectos"

    form = AuthenticationForm()
    return render(request, "AppUsers/login.html", {"form": form, "msg_login": msg_login})


def register(request):

    msg_register = ""
    if request.method == 'POST':

        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # Si los datos ingresados en el form son válidos, con form.save()
            # creamos un nuevo user usando esos datos
            form.save()
            return render(request,"AppRheo/index.html")
        
        msg_register = "Error en los datos ingresados"

    form = UserRegisterForm()     
    return render(request,"AppUsers/registro.html" ,  {"form":form, "msg_register": msg_register})



# Vista de editar el perfil
# Obligamos a loguearse para editar los datos del usuario activo
@login_required
def editar_usuario(request):

    # El usuario para poder editar su perfil primero debe estar logueado.
    # Al estar logueado, podremos encontrar dentro del request la instancia
    # del usuario -> request.user
    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            # Datos que se modificarán
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password1']
            usuario.save()

            # Retornamos al inicio una vez guardado los datos
            return render(request, "AppRheo/index.html")

    else:
        # Cuando el método es GET, podemos mostrar el formulario
        # con datos pre-cargados porque los conocemos del mismo usuario
        datos = {
            'first_name': usuario.first_name,
            'email': usuario.email
        }
        miFormulario = UserEditForm(initial=datos)

    return render(
        request,
        "AppUsers/editar_usuario.html",
        {
            "mi_form": miFormulario,
            "usuario": usuario
        }
    )