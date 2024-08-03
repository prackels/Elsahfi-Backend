from rest_framework import decorators,permissions, status
from rest_framework.response import Response
from expenses.apis.serializers import StationExpSerializer
from expenses.models import StationExpense
from globals.real_time_activity import SendRealTimeActivity


@decorators.api_view(['PUT'])
@decorators.permission_classes([permissions.IsAdminUser])
def update_station_exp (request, stationid) : 
    try : 
        
        try : 
            station = StationExpense.objects.get(id=stationid)
        except StationExpense.DoesNotExist : 
            return Response({
                'message' : 'model with this id does not found'
            },status=status.HTTP_404_NOT_FOUND)
                
        serializer = StationExpSerializer(station,request.data)

        if serializer.is_valid() :
            serializer.save()
            SendRealTimeActivity(
                content="update government expense",
                from_user=request.user
            )
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    except Exception as error : 
        return Response({
            'message' : f'an error accured : {error}'
        },status=status.HTTP_400_BAD_REQUEST)