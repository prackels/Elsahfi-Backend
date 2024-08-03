from rest_framework import decorators,permissions, status
from rest_framework.response import Response
from expenses.apis.serializers import CarsExpensesSerializer
from employee.models import Car
from globals.real_time_activity import SendRealTimeActivity

@decorators.api_view(['POST'])
@decorators.permission_classes([permissions.IsAdminUser])
def create_cars_expenses(request):
    data = request.data.copy()

    try:
        car = Car.objects.get(type_of_car = data.get("car_type"))
    except Car.DoesNotExist:
        return Response({
            "message": "Car doesn't exists"
        }, status=status.HTTP_404_NOT_FOUND)
    try : 
        data["car_type"] = car.pk
        serializer = CarsExpensesSerializer(data=data)
        if serializer.is_valid() : 
            serializer.save()
            SendRealTimeActivity(
                content="create cars expense",
                from_user=request.user
            )
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except Exception as error :
        return Response({
            'message' : f'an error accured : {error}'
        },status=status.HTTP_400_BAD_REQUEST)