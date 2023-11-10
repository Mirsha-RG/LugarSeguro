from rest_framework import serializers
from registro.models import Formulario
from registro.models import Usuario

class FormularioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Formulario
        fields = '__all__'
class UsuarioSerializers(serializers.ModelSerializer):
     class Meta:
        model = Usuario
        fields = '__all__'



        """ la funcion se abre cuando la appi este completa
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['formulario'] = FormularioSerializers(instance.formulario).data
        return response
        
        """