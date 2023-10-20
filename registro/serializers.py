from rest_framework import serializers
from registro.models import Formulario

class FormularioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formulario
        fields = '__all__'