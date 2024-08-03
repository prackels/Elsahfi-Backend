from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.permissions import IsAdminUser
from ....models import CustomerStation
from ...serializers import CustomerStationSerializer
from django.db.models import Sum
from clients_.models import NewCustomer
from clients_.apis.serializers import NewCustomerSerializer


@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_customer_station(request):
    try:
        query= CustomerStation.objects.all()
        serializer= CustomerStationSerializer(query, many= True)
        gasoline_91_quantity = CustomerStation.objects.filter(subject_name='Premium Gasoline 91').aggregate(total_quantity=Sum('quantity'))['total_quantity']
        gasoline_95_quantity = CustomerStation.objects.filter(subject_name='Premium Gasoline 95').aggregate(total_quantity=Sum('quantity'))['total_quantity']
        diesel_quantity = CustomerStation.objects.filter(subject_name='Diesel').aggregate(total_quantity=Sum('quantity'))['total_quantity']
        total_quantity = CustomerStation.objects.aggregate(total_quantity=Sum('quantity'))['total_quantity']


        response_data= {'total_91': gasoline_91_quantity,
                        'total_95': gasoline_95_quantity,
                        'total_diesel': diesel_quantity,
                        'total_sold': total_quantity,
                        'main_data': serializer.data,
                        }
        return Response(response_data, status= HTTP_200_OK)
    except Exception as error:
        return Response(f'sorry there are problem while getting the data :( : {error})', status= HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_customer_orders_byname(request, customer_name):
    try:
        query = CustomerStation.objects.filter(customer_name__customer_name=customer_name).last()
        serializer = CustomerStationSerializer(query, many=False).data
        return Response({
            "data": serializer
        }, status=HTTP_200_OK)
    except Exception as error:
        return Response(f"Sorry, there was a problem while getting the data: {error}", status=HTTP_400_BAD_REQUEST)