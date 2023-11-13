
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
    imagen = models.ImageField(upload_to='imagen')
    status = models.BooleanField(default=True, verbose_name='Status')

    class Meta:
        db_table = 'formulario'



class Usuario(models.Model):
    user = models.CharField(max_length=128, verbose_name="usuario")
    email = models.EmailField(max_length=128, verbose_name="email")
    password = models.CharField(max_length=128, verbose_name="password")
    status = models.BooleanField(default=True, verbose_name='Status')

    class Meta:
        db_table = 'usuarios'


class Likes(models.Model):
    likes = models.IntegerField(default=0)
    nameId = models.ForeignKey(Formulario, on_delete=models.CASCADE, null=True, verbose_name='Usuario')
    usuarioId = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, verbose_name='Usuario')
    status = models.BooleanField(default=True, verbose_name='Status')

    class Meta:
        db_table = 'Likes'

class Dislikes(models.Model):
    dislikes = models.IntegerField(default=0)
    nameId = models.ForeignKey(Formulario, on_delete=models.CASCADE, null=True, verbose_name='Usuario')
    usuarioId = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, verbose_name='Usuario')
    status = models.BooleanField(default=True, verbose_name='Status')

    class Meta:
        db_table = 'Dislikes'