from rest_framework import serializers
from registro.models import Formulario

class FormularioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formulario
        fields = '__all__'
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['formulario'] = FormularioSerializers(instance.formulario).data
        return response