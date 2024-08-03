from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.permissions import IsAdminUser
from ...serializers import CustomerStationSerializer, NewCustomer
from clients_.models import NewCustomer
from ....models import CustomerStation
from django.db.models import Sum, F 

@api_view(['POST'])
@permission_classes([IsAdminUser])
def create_customer_station(request):
    try:
        client_name = request.data.get('customer_name')
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
        data['customer_name'] = new_customer.sequence
        serializer = CustomerStationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=HTTP_200_OK)
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)
    except Exception as error:
        return Response({"message" : f"an error occurred : {error}"}, status=HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_previous_quantity_customer_station(request, customer_name, subject_name):
    try:
        query= CustomerStation.objects.filter(customer_name__customer_name= customer_name, subject_name= subject_name)
        if query.exists():
            previous_quantity_data = query.aggregate(Sum(F('previous_quantity')))
            previous_quantity = previous_quantity_data['previous_quantity'] if 'previous_quantity' in previous_quantity_data else 0
            return Response({"previous_quantity": previous_quantity}, status=HTTP_200_OK)
        else:
            return Response({"previous_quantity": 0}, status= HTTP_200_OK)
    except Exception as error:
        return Response({"message" : f"an error occurred : {error}"}, status=HTTP_400_BAD_REQUEST)
