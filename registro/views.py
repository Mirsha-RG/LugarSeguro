from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm

from registro.serializers import(
    UsuarioSerializers,
    FormularioSerializers,
    LikesSerializer,
)
from registro.models import Usuario, Formulario, Likes
from rest_framework.parsers import MultiPartParser
from django.shortcuts import render, redirect




class CreateLugarAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        formulario_obj = Formulario.objects.create(
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

class ListLugaresAPIVIEW(APIView):
    permission_classes = (AllowAny, )
    def get(self, request):
        registro_list = Formulario.objects.filter(status=True)
        serializer = FormularioSerializers(registro_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class RetrieveFormularioAPIView(APIView):
   permission_classes = (AllowAny, )

   def get(self, request, formulario_id):
        formulario_obj = get_object_or_404(Formulario, pk=formulario_id)
        serializer = FormularioSerializers(formulario_obj, many=False)
        return Response(serializer.data)

   def put(self, request, formulario_id):
        formulario_obj = get_object_or_404(Formulario, pk=formulario_id)
        serializer = FormularioSerializers(instance=formulario_obj, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

   def delete(self, request, formulario_id):
        formulario_obj = get_object_or_404(Formulario, pk=formulario_id)
        formulario_obj.status = False
        formulario_obj.save()
        return Response({'message': 'Eliminado'}, status=status.HTTP_204_NO_CONTENT)



   """class FormularioView(APIView):
        parser_classes = [MultiPartParser]

        def post(self, request):
            imagen = request.data['imagen']
            return Response({'message': 'Imagen cargada correctamente'}) """

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

class ListUsuariosAPIVIEW(APIView):
    permission_classes = (AllowAny, )
    def get(self, request):
       usuarios_list = Usuario.objects.filter(status=True)
       serializer = UsuarioSerializers( usuarios_list, many=True)
       return Response(serializer.data, status=status.HTTP_200_OK)

class RetrieveUsuarioAPIView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, formulario_id):
        usuario_obj = get_object_or_404(Usuario, pk=formulario_id)
        serializer = FormularioSerializers(usuario_obj, many=False)
        return Response(serializer.data)

    def post(self, request, usuario_id):
        usuario_obj = get_object_or_404(Usuario, pk=usuario_id)
        serializer = FormularioSerializers(usuario_obj, many=False)
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
    def post(self, request):
        Like_obj = Like.objects.create(
            usuario = request.data.get('name',''),
            contrasena = request.data.get('contraseña',''),
            lugar = request.data.get('lugar',''),
        )

class ListLikeAPIView(APIView):
    permission_classes = (AllowAny,)
    def get(self, request):
        like_list = Likes.objects.all()
        serializer = UsuarioSerializers(likes_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class RetrieveLikeAPIView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, likes_id):
        like_obj = get_object_or_404(Likes, pk=likes_id)
        serializer = LikesSerializers(like_obj, many=False)
        return Response(serializer.data)

    def post(self, request, likes_id):
        like_obj = get_object_or_404(Likes, pk=likes_id)
        like.votes += 1
        like.save()
        return Response({'message': 'Like agregado', 'votes': like_obj.votes}, status=status.HTTP_200_OK)

    def put(self, request, likes_id):
        like_obj = get_object_or_404(Likes, pk=likes_id)
        serializer = LikeSerializers(instance=like_obj, data=request.data, partial=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, likes_id):
        like_obj = get_object_or_404(Likes, pk=likes_id)
        like_obj.status = False
        like_obj.save()
        return Response({'message': 'Eliminado'}, status=status.HTTP_204_NO_CONTENT)

# Dislike ********************************************************************************************+

class CreateDislikeAPIView(APIView):
    def post(self, request):
        Dislike_obj = Dislike.objects.create(
            usuario = request.data.get('name',''),
            contraseña = request.data.get('descripcion',''),
            lugar = request.data.get('lugar',''),
        )

class ListDislikeAPIView(APIView):
    permission_classes = (AllowAny, )

    def get(self, request):
        dislike_list = Dislikes.objects.all()
        serializer = DislikesSerializers(dislikes_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class RetriveDislikeAPIView(APIView):
    def post(self, request, like_id):
        dislike = get_object_or_404(Likes, pk=dislike_id)
        dislike.votes -= 1
        dislike.save()
        return Response({'message': 'Dislike agregado', 'votes': dislike.votes}, status=status.HTTP_200_OK)


    def put(self, request, likes_id):
        dislike_obj = get_object_or_404(Dislikes, pk=dislike_id)
        serializer = DislikesSerializers(instance=like_obj, data=request.data, partial=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, likes_id):
        dislike_obj = get_object_or_404(Dislikes, pk=dislike_id)
        dislike_obj.status = False
        dislike_obj .save()
        return Response({'message': 'Eliminado'}, status=status.HTTP_204_NO_CONTENT)

#Registro Usuario codigo de prueba
"""
class RetrieveRegistroAPIView(APIView):
    permission_classes = (AllowAny)

    def SignUpView(request):
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)  # Iniciar sesión después del registro
                return redirect('home')  # Redirigir a la página principal u otra vista
        else:
            form = UserCreationForm()
        return render(request, 'registration/signup.html', {'form': form})

    def LoginView(request):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)


            if user is not None:
                loggin(request, user)
            return redirect('LoginView'), Response({'message': 'Los datos ingresados son incorrectos'}, status=status.HTTP_204_NO_CONTENT)

        else:
            form = AuthenticationForm()
            return render(request, 'login.html', {'form': form})

    def LogoutView(request):
        logout(request)
        return redirect('LoginView')
"""