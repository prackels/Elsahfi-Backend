from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.permissions import IsAdminUser
from ....models import DeiannaCustomer
from ...serializers import DeiannaCustomerSerializer
from django.db.models import Sum

@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_deianna_customer(request):
    try:
        query= DeiannaCustomer.objects.all()
        serializer= DeiannaCustomerSerializer(query, many= True)
        total_trips = DeiannaCustomer.objects.count()
        total_value_rent = DeiannaCustomer.objects.aggregate(total_value=Sum('value_rent'))['total_value']
        total_quantity= DeiannaCustomer.objects.aggregate(total_quantity=Sum('quantity'))['total_quantity']
        response_data= {'total_trips': total_trips,
                        'total_value_rent': total_value_rent,
                        'total_quantity': total_quantity,
                        'data': serializer.data,
                        }
        return Response(response_data, status= HTTP_200_OK)
    except Exception as error:
        return Response(f'sorry there are problem while getting the data :( : {error})', status= HTTP_400_BAD_REQUEST)