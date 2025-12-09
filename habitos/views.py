from django.shortcuts import render
from rest_framework.decorators import action
from .models import UsuarioModel, HabitoModel
from .serializers import UsuarioSerializer, HabitoSerializer
from rest_framework import viewsets, filters
from rest_framework.response import Response

def index(request):
    return render(request, 'index.html')

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset= UsuarioModel.objects.all()
    serializer_class= UsuarioSerializer
    filter_backends= [filters.SearchFilter, filters.OrderingFilter]
    search_fields= ['nombre', 'apodo']
    ordering_fields= ['apodo', 'nombre']


    #Login, verifica que el correo y contraseña sean correctos

    @action(detail=False, methods=['post'])
    def login(self, request):
        correo= request.data.get('correo')
        contrasena= request.data.get('contrasena')

        try:
            usuario= UsuarioModel.objects.get(correo= correo, contrasena= contrasena)

        except UsuarioModel.DoesNotExist:
            return Response({"error": "correo o contraseña incorrecto"}, estatus= 400)
        
        return Response({
            "mensaje": "Datos Verificados",
            "usuario_id": usuario.id,
            "contrasena": usuario.contrasena,
        })



class HabitoViewSet(viewsets.ModelViewSet):
    queryset= HabitoModel.objects.all()
    serializer_class= HabitoSerializer
    filter_backends= [filters.SearchFilter, filters.OrderingFilter]
    search_fields= ['nombre', 'categoria', 'estado']
    ordering_fields= ['categoria','nombre', 'descripcion', 'hora_inicio', 'lugar']