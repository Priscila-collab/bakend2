from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator,MinLengthValidator,MaxLengthValidator
from .Validadores import validacion_numeros,validar_telefono,validar_nombres
from .choices import CARGO
class Empleado(models.Model):
    cedula = models.CharField(max_length=10,primary_key=True, validators=[MinLengthValidator(10), validacion_numeros])
    nombre = models.CharField(max_length=50, validators=[MaxLengthValidator(50), validar_nombres])
    apellido = models.CharField(max_length=50, validators=[MaxLengthValidator(50), validar_nombres])
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    class Meta:
        db_table = 'Empleado'
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
    def __str__(self):
         return self.cedula

class Cliente(models.Model):
    cedula = models.CharField(max_length=10,primary_key=True, validators=[MinLengthValidator(10), validacion_numeros])
    nombre = models.CharField(max_length=50, validators=[MaxLengthValidator(50), validar_nombres])
    apellido = models.CharField(max_length=50, validators=[MaxLengthValidator(50), validar_nombres])
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)

class Meta:
        db_table = 'Cliente'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

        def __str__(self):
             return self.cedula

class Producto(models.Model):
    codigo = models.CharField(max_length=5, primary_key=True)
    nombre = models.CharField(max_length=50)
    precio = models.CharField(max_length=50)
    class Meta:
        db_table = 'Producto'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

class Categoria(models.Model):
    nom_cat = models.CharField(max_length=50)
    descripcion=models.CharField(max_length=20)
    class Meta:
        db_table = 'Categoria'
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
