from rest_framework import decorators, permissions, status
from rest_framework.response import Response
from ..models import User
from .serializers import UserSerializer

@decorators.api_view(['POST'])
@decorators.permission_classes([permissions.IsAdminUser])
def CreateUser (request) : 
    try :
        
        full_name = request.data.get('full_name')
        email = request.data.get('email')
        password = request.data.get('password')

        if not full_name or not email or not password : 
            return Response({
                'message' : 'please make sure that you enter full_name, email and password fields'
            },status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(email=email).exists() : 
            return Response({
                'message' : 'this email already taken by another user'
            },status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(
            email = email,
            password = password,
            full_name = full_name,
        )

        user.save()

        return Response(UserSerializer(user).data,status=status.HTTP_200_OK)

    except Exception as error :
        return Response({
            "message" : f"an error accured : {error}"
        },status=status.HTTP_400_BAD_REQUEST)