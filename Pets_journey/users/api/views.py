from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import User
from users.api.serializers import UserSerializer
from rest_framework.status import HTTP_200_OK

class UsersView(APIView):
    @staticmethod
    def get(request):
        users = User.objects.all()
        return Response(data=UserSerializer(users , many=True).data,status=HTTP_200_OK)
