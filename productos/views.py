from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)

from django.shortcuts import render
from .models import Producto
from .forms import ProductoForm, EditarForm

productos = []


def listar_productos(request):
    query = request.GET.get('buscar', '')
    if query:
        productos = Producto.objects.filter(nombre__icontains=query)
    else:
        productos = Producto.objects.all()
    return render(request, 'listar.html', {'productos': productos, 'query': query})

def editar_producto(request, id):
    context ={}
    obj = get_object_or_404(Producto, id = id)
    form = EditarForm(request.POST or None, instance = obj)
 

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            productos = Producto.objects.all()
            return render(request, 'listar.html', {'productos': productos})
    else:
        context["form"] = form
 
    return render(request, "editar.html", context)

def eliminar_producto(request, id):
    obj = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        obj.delete()
        productos = Producto.objects.all()
        return render(request, 'listar.html', {'productos': productos})
    return render(request, 'eliminar.html', {'producto': obj})

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            productos = Producto.objects.all()
            return render(request, 'listar.html', {'productos': productos})
    else:
        form = ProductoForm()
    return render(request, 'agregar.html', {'formulario': form})

