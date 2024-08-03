from rest_framework import decorators,permissions, status
from rest_framework.response import Response
from expenses.models import CarsExpenses
from globals.real_time_activity import SendRealTimeActivity


@decorators.api_view(['DELETE'])
@decorators.permission_classes([permissions.IsAdminUser])
def delete_cars_expenses(request, pk):
    try : 
        try : 
            station = CarsExpenses.objects.get(sequence=pk)
        except CarsExpenses.DoesNotExist :
            return Response({
                'message' : 'model with this id does not found'
            },status=status.HTTP_404_NOT_FOUND)
        station.delete()
        SendRealTimeActivity(
            content="delete cars expense",
            from_user=request.user
        )
        return Response('deleted', status= status.HTTP_200_OK)
    except Exception as error : 
        return Response({
            'message' : f'an error accured : {error}'
        },status=status.HTTP_400_BAD_REQUEST)