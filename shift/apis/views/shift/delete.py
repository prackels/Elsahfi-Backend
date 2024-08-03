from rest_framework import status, decorators, permissions
from rest_framework.response import Response
from ....models import Shift
from django.utils.timezone import datetime



@decorators.api_view(['DELETE'])
@decorators.permission_classes([permissions.IsAdminUser])
def DeleteShift (request, shift_uid) : 
    try : 
        try : 
            shift = Shift.objects.get(uid=shift_uid,is_active=True)
        except Shift.DoesNotExist : 
            return Response({
                'message' : 'no shift with this uid'
            },status=status.HTTP_404_NOT_FOUND)
        
        shift.is_active = False
        shift.end_at = datetime.now()

        shift.save()
        return Response({
            'message' : 'shift deleted successfully'
        },status=status.HTTP_200_OK)
    

    except Exception as error :
        return Response({
            'message' : f'an error accured : {error}'
        },status=status.HTTP_400_BAD_REQUEST)