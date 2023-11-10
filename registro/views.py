from rest_framework import status

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm

from registro.models import Formulario
from registro.serializers import FormularioSerializers
from registro.models import Usuario
from registro.serializers import UsuarioSerializers
from rest_framework.parsers import MultiPartParser


class RetrieveFormulario(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        registro_list = Formulario.objects.all()
        serializer = FormularioSerializers(registro_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CreateLugar(APIView):
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

"""class FormularioView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request):
        imagen = request.data['imagen']
        return Response({'message': 'Imagen cargada correctamente'}) """


class RetrieveFormularioAPIView(APIView):
    permission_classes = (AllowAny)

    def get(self, request, formulario_id):
        formulario_obj = get.object_or_404(Formulario, pk=formulario_id)
        serializer = FormularioSerializers(formulario_obj, many=False)
        return Response(serializer.data)

    def put(self, request, formulario_id):
        formulario_obj = get.object_or_404(Formulario, pk=formulario_id)
        serializer = FormularioSerializers(instance=formulario_obj, data=request.data, partial=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, formulario_id):
        formulario_obj = get.object_or_404(Formulario, pk=formulario_id)
        formulario_obj.status = False
        formulario_obj.save()
        return Response({'message': 'Eliminado'}, status=status.HTTP_204_NO_CONTENT)

class RetrieveUsuario(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        usuario_list = Usuario.objects.all()
        serializer = UsuarioSerializers(usuario_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
class CreateUsuario(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        usuario_obj = Usuario.objects.create(
            user=request.data.get('name', ''),
            email=request.data.get('email', ''),
            password=request.data.get('contraseña', ''),

            )

        return Response({'message': 'Creado'}, status=status.HTTP_201_CREATED)


class RetrieveUsuarioAPIView(APIView):
    permission_classes = (AllowAny, )

    def get(self, request, usuario_id):
        usuario_obj = get.object_or_404(Usuario, pk=usuario_id)
        serializer = FormularioSerializers(formulario_obj, many=False)
        return Response(serializer.data)

    def put(self, request, usuario_id):
        usuario_obj = put.object_or_404(Usuario, pk=usuario_id)
        serializer = UsuarioSerializers(instance=formulario_obj, data=request.data, partial=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, usuario_id):
        formulario_obj = get.object_or_404(Formulario, pk=usuario_id)
        formulario_obj.status = False
        formulario_obj.save()
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