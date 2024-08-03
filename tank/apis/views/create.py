from rest_framework import status, decorators, permissions
from rest_framework.response import Response
from tank.apis.serializer import TankSerializer, Tank

@decorators.api_view(['POST'])
@decorators.permission_classes([permissions.IsAdminUser])
def CreateTank (request) : 
    try :
        material = request.data.get('material')
        serializer = TankSerializer(data=request.data)
        if serializer.is_valid() :
            if Tank.objects.filter(material=material).exists() : 
                return Response(
                    {"message":"the tank with this material already exists!"}
                ,status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except Exception as error :
        return Response({
            'message' : f'an error occurred : {error}'
        },status=status.HTTP_400_BAD_REQUEST)