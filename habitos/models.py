from django.db import models

class UsuarioModel(models.Model):

    apodo= models.CharField(max_length=30 )
    nombre= models.CharField(max_length=60)
    correo= models.EmailField(max_length=100, unique=True)
    contrasena= models.CharField(max_length=16)

class HabitoModel(models.Model):

    ESTADO_HABITO_CHOICES={
        ('CO', 'Completado'),
        ('RE', 'Realizando'),
        ('FI', 'Finalizado'),
        ('IN', 'Inactivo'),

    }

    CATEGORIA_HABITO_CHOICES= {

        ('TR', 'Trabajo'),
        ('OC', 'Ocio'),
        ('CO', 'Compromiso'),
        ('FA', 'Familia'),
        ('DE', 'Deporte'),

    }

    nombre= models.CharField(max_length=30)
    descripcion= models.CharField()
    hora_inicio= models.DateTimeField()
    hora_final= models.DateTimeField()
    lugar= models.CharField(max_length=40)
    estado= models.CharField(max_length=2, choices=ESTADO_HABITO_CHOICES)
    categoria= models.CharField(max_length=2, choices=CATEGORIA_HABITO_CHOICES)
    usuario= models.ForeignKey(UsuarioModel, on_delete=models.CASCADE, related_name='habitos')

