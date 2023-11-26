from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import AnonymousUser

from registro.serializers import(
    UsuarioSerializers,
    LugarSerializers,
    LikesSerializer,
    DislikesSerializer,
)

from registro.models import Usuario, Lugar, Likes
from rest_framework.parsers import MultiPartParser
from django.shortcuts import render, redirect




class CreateLugarAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
       lugar_obj= Lugar.objects.create(
            nombre = request.data.get('name',''),
            descripcion = request.data.get('descripcion',''),
            estado = request.data.get('estado',''),
            ciudad = request.data.get('ciudad',''),
            colonia = request.data.get('colonia',''),
            calle = request.data.get('calle',''),
            numero = request.data.get('numero',''),
            cp = request.data.get('cp',''),
            imagen = request.data.get('imagen',''),

        )
       return Response ({'message':'Creado'}, status=status.HTTP_201_CREATED)


class RetrieveLugarAPIView(APIView):
   permission_classes = (AllowAny, )

   def get(self, request, lugar_id):
        lugar_obj = get_object_or_404(Lugar, pk=lugar_id)
        total_likes = lugar_obj.likes.count()
        total_dislikes = lugar_obj.dislikes.count()
        serializer = LugarSerializers(lugar_obj, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

   def put(self, request, lugar_id):
        lugar_obj = get_object_or_404(Lugar, pk=lugar_id)
        serializer = LugarSerializers(instance=lugar_obj, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

   def delete(self, request, lugar_id):
        lugar_obj = get_object_or_404(Lugar, pk=lugar_id)
        lugar_obj.status = False
        lugar_obj.save()
        return Response({'message': 'Eliminado'}, status=status.HTTP_204_NO_CONTENT)

#Listar lugares ***********************************************************************************
class ListLugaresAPIVIEW(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        lugares_list = Lugar.objects.filter(status=True)

      #total de likes para cada lugar
        lugares_data = []
        for lugar in lugares_list:
            total_likes = lugar.likes.count()
            serializer = LugarSerializers(lugar, many=False)
            lugar_data = serializer.data
            lugar_data['total_likes'] = total_likes
            lugares_data.append(lugar_data)

        return Response(lugares_data, status=status.HTTP_200_OK)



#Usuario********************************************************************************************************

class CreateUsuarioAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        usuario_obj = Usuario.objects.create(
            user=request.data.get('name', ''),
            email=request.data.get('email', ''),
            password=request.data.get('contraseña', ''),

            )

        return Response({'message': 'Creado'}, status=status.HTTP_201_CREATED)



class RetrieveUsuarioAPIView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, lugar_id):
        usuario_obj = get_object_or_404(Usuario, pk=lugar_id)
        serializer = UsuarioSerializers(usuario_obj, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, usuario_id):
        usuario_obj = get_object_or_404(Usuario, pk=usuario_id)
        serializer = UsuarioSerializers(usuario_obj, many=False)
        return Response(serializer.data)

    def put(self, request, usuario_id):
        usuario_obj = get_object_or_404(Usuario, pk=usuario_id)
        serializer = UsuarioSerializers(instance=usuario_obj, data=request.data, partial=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, usuario_id):
        usuario_obj = get_object_or_404(Usuario, pk=usuario_id)
        usuario_obj.status = False
        usuario_obj.save()
        return Response({'message': 'Eliminado'}, status=status.HTTP_204_NO_CONTENT)

#Imagen **************************************************************************************

class CreateImagenAPIView(APIView):

    def post(self, request):
        imagen_obj = Imagen.objects,create(
            usuario = request.data.get('name', ''),
            contrasena = request.data.get('contraseña'),
            lugar = request.data.get('lugar'),
        )

#Likes ******************************************************************************************************************

class CreateLikeAPIView(APIView):
    def post(self, request, lugar_id):

        if not request.user.is_authenticated:
            return Response({'detail': 'Debes iniciar sesión para dar like'}, status=status.HTTP_401_UNAUTHORIZED)

        # Obtener el lugar específico
        lugar = Lugar.objects.get(pk=lugar_id)

        # Verificar si el usuario ya dio like al lugar
        if Likes.objects.filter(usuario =usuario, name=lugar).exists():
            return Response({'detail': 'Ya diste like a este lugar'}, status=status.HTTP_400_BAD_REQUEST)

            # Crear o recuperar el like existente
        like, created = Likes.objects.get_or_create(usuario_Id=usuario, name_Id=lugar)
        lugar.likes += 1
        lugar.save()

        # Serializar y responder con la información del like
        serializer = LikeSerializer(like)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, likes_id):
        like_obj = get_object_or_404(Likes, pk=likes_id)
        like_obj.status = False
        like_obj.save()
        return Response({'message': 'Eliminado'}, status=status.HTTP_204_NO_CONTENT)

# Dislike ********************************************************************************************+

class CreateDislikeAPIView(APIView):
    def post(self, request, lugar_id):
        if not request.user.is_authenticated:
            return Response({'detail': 'Debes iniciar sesión para dar like'}, status=status.HTTP_401_UNAUTHORIZED)

        lugar = Lugar.objects.get(pk=lugar_id)

        if Dislikes.objects.filter(usuario_Id=usuario, name_Id=lugar).exists():
            return Response({'detail': 'Ya diste dislike a este lugar'}, status=status.HTTP_400_BAD_REQUEST)


        dislike, created = Dislikes.objects.get_or_create(usuario_Id=usuario, name_Id=lugar)
        lugar.dislikes += 1
        lugar.save()

        serializer = DislikeSerializer(dislike)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, dislikes_id):
        dislike = get_object_or_404(Dislikes, pk=dislikes_id)
        dislike.status = False
        dislike.save()
        return Response({'message': 'Eliminado'}, status=status.HTTP_204_NO_CONTENT)


