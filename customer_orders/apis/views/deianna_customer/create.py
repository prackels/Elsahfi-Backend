from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.permissions import IsAdminUser
from ...serializers import DeiannaCustomerSerializer
from clients_.models import NewCustomer
from clients_.apis.serializers import NewCustomerSerializer
from employee.models import Car

@api_view(['POST'])
@permission_classes([IsAdminUser])
def create_deianna_customer(request):
    try:
        client_name = request.data.get('customer_name',None)

        if client_name is None :
            return Response({
                'message' : "customer_name field can not be empty"
            },status=HTTP_400_BAD_REQUEST)
        
        new_customer = NewCustomer.objects.filter(customer_name=client_name)

        if new_customer.count() == 0 :
                return Response({
                    'message' : f"there is no customer name : '{client_name}'"
                },status=HTTP_400_BAD_REQUEST)

        new_customer = new_customer.last()
        data = request.data.copy()
        try:
            car = Car.objects.get(type_of_car = data.get("car_type"))
        except Car.DoesNotExist:
            return Response({
                "message": "Car doesn't exists"
            }, status=status.HTTP_404_NOT_FOUND)
        data['customer_name'] = new_customer.sequence
        data['car_type'] = car.pk
        serializer = DeiannaCustomerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=HTTP_200_OK)
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)
    except Exception as error:
        return Response({"message" : f"an error accured : {error}"}, status=HTTP_400_BAD_REQUEST)