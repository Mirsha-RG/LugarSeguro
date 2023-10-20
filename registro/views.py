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


