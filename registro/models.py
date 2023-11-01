
from django.db import models

# Create your models here.


class Formulario(models.Model):
    nombre = models.CharField(max_length=128, verbose_name='Nombre')
    descripcion = models.CharField(max_length=128, verbose_name='Descripción')
    estado = models.CharField(max_length=128, verbose_name='Estado')
    ciudad = models.CharField(max_length=128, verbose_name='Ciudad')
    colonia = models.CharField(max_length=128, verbose_name='Colonia')
    calle = models.CharField(max_length=128, verbose_name='Calle')
    numero = models.IntegerField(default=0, verbose_name='Numero')
    cp = models.IntegerField(default=0, verbose_name='Código Postal')
    registrado = models.BooleanField(default=False, verbose_name='Ya existe')
    imagen = models.ImageField(upload_to='imagenes/', verbose_name='Imagen')
    status = models.BooleanField(default=True, verbose_name='Status')

    class Meta:
        db_table = 'formulario'





