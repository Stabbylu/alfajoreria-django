from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('conocenos', views.conocenos, name = 'conocenos'),
    path('visitanos', views.visitanos, name = 'visitanos'),
    path('alfajores', views.alfajores, name = 'alfajores'),
    path('oEspeciales', views.oEspeciales, name = 'oEspeciales'),
    path('ofertas', views.ofertas, name = 'ofertas'),
    path('contacto', views.contacto, name ='contacto'),
    path('registro', views.registro, name ='registro'),
    path('agregar-producto', views.agregar_producto, name ='agregar_producto'),
    path('listar-productos', views.listar_productos, name ='listar_productos'),
    path('modificar-producto/<id>/', views.modificar_producto, name ='modificar_producto'),
    path('eliminar-producto/<id>/', views.eliminar_producto, name ='eliminar_producto'),
]