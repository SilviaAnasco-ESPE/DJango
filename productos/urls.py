from django.urls import path
from .views import editar_producto, eliminar_producto, agregar_producto
from . import views

urlpatterns = [
    # URLs de vistas normales
    path('', views.listar_productos, name='listar_productos'),
    path('<id>/editar', editar_producto, name='editar_producto'),
    path('<id>/eliminar', eliminar_producto, name='eliminar_producto'),
    path('agregar', agregar_producto, name='agregar_producto'),
]