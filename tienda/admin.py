from django.contrib import admin
from .models import Producto,Categoria, Contacto
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio","unidades", "stock"]
    list_editable = ["precio","unidades","stock"]

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria)
admin.site.register(Contacto)