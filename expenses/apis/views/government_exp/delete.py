from rest_framework import decorators,permissions, status
from rest_framework.response import Response
from expenses.models import GovernmentExpense
from globals.real_time_activity import SendRealTimeActivity


@decorators.api_view(['DELETE'])
@decorators.permission_classes([permissions.IsAdminUser])
def delete_gov_station_exp (request, stationid) : 
    try : 
        
        try : 
            station = GovernmentExpense.objects.get(sequence=stationid)
        except GovernmentExpense.DoesNotExist : 
            return Response({
                'message' : 'model with this id does not found'
            },status=status.HTTP_404_NOT_FOUND)
                
        station.delete()

        SendRealTimeActivity(
            content="delete government expense",
            from_user=request.user
        )
        return Response('deleted', status= status.HTTP_200_OK)
    except Exception as error : 
        return Response({
            'message' : f'an error accured : {error}'
        },status=status.HTTP_400_BAD_REQUEST)