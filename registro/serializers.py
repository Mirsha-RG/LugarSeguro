from rest_framework import serializers
from registro.models import Lugar
from registro.models import Usuario
from registro.models import Likes
from registro.models import Dislikes

class LugarSerializers(serializers.ModelSerializer):
    class Meta:
        model = Lugar
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
        response = super().to_representation(instance.lugar)
        response['nombre'] = LugarSerializers(instance.lugar).data
        return response

        def to_representation(self, instance):
            response = super().to_representation(instance.lugar)
            response['user'] = UsuarioSerializers(instance.lugar).data
            return response

class DislikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dislikes
        fields = ['__all__']

        def to_representation(self, instance):
            response = super().to_representation(instance.lugar)
            response['nombre'] = LugarSerializers(instance.lugar).data
            return response

            def to_representation(self, instance):
                response = super().to_representation(instance.lugar)
                response['user'] = UsuarioSerializers(instance.lugar).data
                return response

