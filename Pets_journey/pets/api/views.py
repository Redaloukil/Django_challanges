from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Dog , Cat
from pets.api.serializers import DogSerializer , CatSerializer
from rest_framework.status import HTTP_200_OK

class DogsView(APIView):
    @staticmethod
    def get(request):
        dogs = Dog.objects.all()
        return Response(data=DogSerializer(dogs , many=True).data,status=HTTP_200_OK)

class CatsView(APIView):
    @staticmethod
    def get(request):
        cats = Cat.objects.all()
        return Response(data=CatSerializer(cats , many=True).data ,status=HTTP_200_OK)
