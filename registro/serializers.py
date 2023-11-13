from rest_framework import serializers
from registro.models import Formulario
from registro.models import Usuario
from registro.models import Likes

class FormularioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Formulario
        fields = '__all__'

class UsuarioSerializers(serializers.ModelSerializer):
     class Meta:
        model = Usuario
        fields = '__all__'

class LikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Likes
        fields = ['__all__']

    def to_representation(self, instance):
        response = super().to_representation(instance.formulario)
        response['nombre'] = FormularioSerializers(instance.formulario).data
        return response

        def to_representation(self, instance):
            response = super().to_representation(instance.formulario)
            response['user'] = UsuarioSerializers(instance.formulario).data
            return response




        """ la funcion se abre cuando la appi este completa
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['formulario'] = FormularioSerializers(instance.formulario).data
        return response
        
        """