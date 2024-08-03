from rest_framework import decorators,permissions, status
from rest_framework.response import Response
from ...serializers import CarsSerializer
from ....models import NewCustomer


@decorators.api_view(['POST'])
@decorators.permission_classes([permissions.IsAdminUser])
def create_car_for_the_client(request):
    data = request.data.copy()

    try:
        customer = NewCustomer.objects.get(customer_name = data.get("customer"))
    except NewCustomer.DoesNotExist:
        return Response({
            "message": "Customer doesn't exists"
        }, status=status.HTTP_404_NOT_FOUND)
    try : 
        data["customer"] = customer.pk
        serializer = CarsSerializer(data= data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except Exception as error:
        return Response({"message" : f"an error occurred : {error}"}, status=status.HTTP_400_BAD_REQUEST)