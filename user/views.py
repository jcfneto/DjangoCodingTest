from rest_framework import exceptions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UserSerializer


@api_view(['POST'])
def register(request):

    data = request.data

    if data['password'] != data['password_confirm']:
        raise exceptions.APIException('Password does not match!')

    serializer = UserSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status.HTTP_201_CREATED)
