from rest_framework import status, decorators, permissions
from rest_framework.response import Response
from tank.apis.serializer import Tank



@decorators.api_view(['DELETE'])
@decorators.permission_classes([permissions.IsAdminUser])
def DeleteTank (request,tankid) : 
    try :

        
        try : 
            tank = Tank.objects.get(id=tankid)
        except Tank.DoesNotExist :
            return Response({
                'message' : "tank not found"
            },status=status.HTTP_404_NOT_FOUND)
        
        tank.delete()

        return Response({
            'message' : 'tank deleted successfully'
        },status=status.HTTP_200_OK)

    except Exception as error :
        return Response({
            'message' : f'an error accured : {error}'
        },status=status.HTTP_400_BAD_REQUEST)