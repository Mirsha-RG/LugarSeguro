from rest_framework import status

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from registro.models import Formulario
from registro.serializers import FormularioSerializer
from rest_framework.parsers import MultiPartParser


class RetrieveFormulario(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        registro_list = Formulario.objects.all()
        serializer = FormularioSerializer(registro_list, many=True)

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

class FormularioView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request):
        imagen = request.data['imagen']
        return Response({'message': 'Imagen cargada correctamente'})


class RetrieveFormularioAPIView(APIView):
    permission_classes = (AllowAny)

    def get(self, request, formulario_id):
        formulario_obj = Formulario.objects_or_404(Formulario, pk=formulario_id)
        serializer = FormularioSerializer(author_obj)
        return Response(serializer.data)

    def put(self, request, formulario_id):
        formulario_obj = Formulario.objects_or_404(Formulario, pk=formulario_id)
        serializer = FormularioSerializer(instance=author_obj, data=request.data, partial=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, formulario_id):
        formulario_obj = Formulario.objects_or_404(Formulario, pk=formulario_id)
        formulario_obj.status = False
        formulario_obj.save()
        return Response({'message': 'Eliminado'}, status=status.HTTP_204_NO_CONTENT)

