from rest_framework import decorators,permissions, status
from rest_framework.response import Response
from expenses.apis.serializers import CarsExpensesSerializer
from expenses.models import CarsExpenses
from globals.real_time_activity import SendRealTimeActivity


@decorators.api_view(['PUT'])
@decorators.permission_classes([permissions.IsAdminUser])
def update_cars_expenses(request, pk):
    try : 
        
        try : 
            station = CarsExpenses.objects.get(sequence=pk)
        except CarsExpenses.DoesNotExist : 
            return Response({
                'message' : 'model with this id does not found'
            },status=status.HTTP_404_NOT_FOUND)
                
        serializer = CarsExpensesSerializer(station,data=request.data)

        if serializer.is_valid() :
            serializer.save()
            SendRealTimeActivity(
                content="update cars expense",
                from_user=request.user
            )
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    except Exception as error : 
        return Response({
            'message' : f'an error accured : {error}'
        },status=status.HTTP_400_BAD_REQUEST)