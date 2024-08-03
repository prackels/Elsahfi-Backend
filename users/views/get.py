from rest_framework import decorators, permissions, status
from rest_framework.response import Response
from .serializers import UserSerializer
from ..models import User

@decorators.api_view(["GET"])
@decorators.permission_classes([permissions.IsAdminUser])
def get_all_users (request):
    try :
        queryset = User.objects.all()
        serializer = UserSerializer(queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    except Exception as error :
        return Response({
            'message' : f'an error accured : {error}'
        },status=status.HTTP_400_BAD_REQUEST)


@decorators.api_view(["GET"])
@decorators.permission_classes([permissions.IsAuthenticated])
def get_user_info (request) :
    try :
        user = request.user
        return Response({
            'full_name' : user.full_name,
            'email' : user.email,
            'is_superuser' : user.is_superuser
        },status=status.HTTP_200_OK)
    except Exception as error :
        return Response({
            'message' : f'an error accured : {error}'
        },status=status.HTTP_400_BAD_REQUEST)
