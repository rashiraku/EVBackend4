from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.hashers import check_password
from .models import UsuarioModel, HabitoModel


class HabitoSerializer(serializers.ModelSerializer):

    hora_inicio = serializers.DateTimeField(
    format="%Y-%m-%dT%H:%M",
    input_formats=["%Y-%m-%dT%H:%M", "%Y-%m-%d %H:%M"]
    )
    hora_final = serializers.DateTimeField(
    format="%Y-%m-%dT%H:%M",
    input_formats=["%Y-%m-%dT%H:%M", "%Y-%m-%d %H:%M"]
    )



    class Meta:
        model= HabitoModel
        fields= '__all__'


class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        
        habitos= HabitoSerializer( many=True, read_only=True)

        model= UsuarioModel
        fields= '__all__'

class CustomTokenObtainSerializer(TokenObtainPairSerializer):

   # correo= serializers.EmailField()
   # contrasena= serializers.CharField(write_only=True)

    username_field= 'correo'

    def validates(self, attrs):
        correo= attrs.get('correo')
        contrasena= attrs.get('contrasena')

        try:
            usuario= UsuarioModel.objects(correo=correo)
        except UsuarioModel.DoesNotExist:
            raise serializers.ValidationError("Correo o contraseña invalidos")
        
        if usuario.contrasena != contrasena:
            raise serializers.ValidationError("Correo o contraseña invalidos")
        
        data= super().validate({})
        data['access']= self.get_token(usuario).access_token
        data['refresh']= self.get_token(usuario)
        data['usuario']= {
            'id': usuario.id,
            'nombre': usuario.nombre,
            'correo': usuario.correo,

        }

        return data
    