from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ContactoForm,CustomeUserCreationForm,ProductoForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required,permission_required

# Create your views here.
def index(request):
    context={}
    return render(request, 'tienda/index.html',context)

def alfajores(request):
    productos = Producto.objects.all()
    context={"productos":productos}
    return render(request,'tienda/alfajores.html',context)

def oEspeciales(request):
    context={}
    return render(request,'tienda/oEspeciales.html',context)

def ofertas(request):
    context={}
    return render(request,'tienda/ofertas.html',context)

def conocenos(request):

    historia_p1 = "Desde muy joven, Amanda, dueña de “Pipo alfajorería”, mostró un gran amor por los dulces que preparaba su abuela, en especial por los alfajores, una delicia tradicional que aprendió a hacer gracias a ella. A los 18 años y debido a dificultades económicas, Amanda decidió comenzar a vender alfajores por las calles de su ciudad."
    historia_p2 = "Con un carrito lleno de alfajores caseros y una sonrisa, Amanda recorría plazas, mercados y eventos locales. Su dedicación y la calidad de sus productos hicieron que rápidamente se ganara una clientela fiel. A pesar de las dificultades y los desafíos de la vida de un vendedor ambulante, Amanda nunca perdió la pasión por lo que hacía."
    historia_p3 = "A medida que sus alfajores ganaban popularidad, Amanda comenzó a soñar con abrir su propia tienda. Apasionada de la estética victoriana, soñaba con un lugar que combinara su amor por los alfajores y esa elegante época. Durante siete años, ahorró cada peso que pudo, se educó en administración y perfeccionó sus recetas."
    historia_p4 = "Finalmente, a los 25 años, Amanda logró abrir su alfajorería-cafetería, ""Pipo alfajorería"", en el corazón de su ciudad y ha logrado ser un lugar muy querido por sus visitantes. Amanda continúa dedicándose a sus alfajores siempre buscando nuevas formas de sorprender y deleitar a sus clientes con su creatividad culinaria."
    context={"historia_p1":historia_p1,"historia_p2":historia_p2,"historia_p3":historia_p3,"historia_p4":historia_p4}
    return render(request, 'tienda/conocenos.html',context)

def visitanos(request):
    context={}
    return render(request, 'tienda/visitanos.html',context)

def contacto(request):
    context={'form': ContactoForm()}

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            context["mensaje"] = "Mensaje enviado exitosamente..."
        else:
            context["form"] = formulario

    return render(request, 'tienda/contacto.html',context)

def registro(request):
    context={'form': CustomeUserCreationForm()}

    if request.method == 'POST':
        formulario = CustomeUserCreationForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username = formulario.cleaned_data["username"], password= formulario.cleaned_data["password1"])
            login(request,user)
            messages.success(request, "Te has registrado correctamente!")
            return redirect(to="index")
        context["form"] = formulario

    return render(request, 'registration/registro.html',context)

@permission_required('tienda.add_producto')
def agregar_producto(request):

    context={'form': ProductoForm()}

    if request.method == 'POST':
        formulario = ProductoForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "¡Producto agregado correctamente!")
            return redirect(to="listar_productos")
        else:
            context["form"] = formulario

    return render(request, 'productos/agregar.html', context)

@permission_required('tienda.view_producto')
def listar_productos(request):
    
    productos = Producto.objects.all()

    context={
        'productos': productos
    }

    return render(request, 'productos/listar.html', context)

@permission_required('tienda.change_producto')
def modificar_producto(request, id):

    producto = get_object_or_404(Producto, id=id)

    context = {'form':ProductoForm(instance=producto)}

    if request.method == 'POST':
        formulario = ProductoForm(request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "¡Producto modificado correctamente!")
            return redirect(to="listar_productos")
        else:
            context["form"] = formulario

    return render(request, 'productos/modificar.html',context)

@permission_required('tienda.delete_producto')
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, "Producto eliminado")
    return redirect(to="listar_productos")
