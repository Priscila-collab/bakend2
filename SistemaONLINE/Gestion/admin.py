from django.contrib import admin
from .models import Empleado,Producto,Categoria,Cliente

admin.site.register(Empleado)
class Empleado(admin.ModelAdmin):
   list_display =(' cedula','nombre','apellido','direccion','telefono')
   search_fields =('cedula','nombre')
   list_filters =('cedula')
admin.site.register(Cliente)
class Cliente(admin.ModelAdmin):
   list_display =('cedula','nombre','apellido','direccion','telefono')
   search_fields =('codigo','nombre')
   list_filters =('nombre')

admin.site.register(Producto)
class Producto(admin.ModelAdmin):
   list_display =('codigo','nombre','precio')
   search_fields =('codigo','nombre')
   list_filters =('nombre')

admin.site.register(Categoria)
class Categoria(admin.ModelAdmin):
   list_display =('nom_cat','descripcion')
   search_fields =('nom_cat')
   list_filters =('nom_cat')
