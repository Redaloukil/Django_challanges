from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK


class ApiStart(APIView):
    @staticmethod
    def get(request):
        return Response(data="Welcome to the api" , status=HTTP_200_OK)
    