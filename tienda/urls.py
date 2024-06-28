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
    path('registro', views.registro, name ='registro')
]