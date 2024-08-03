from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.permissions import IsAdminUser
from ....models import TrillaCustomer
from ...serializers import TrillaCustomerSerializer
from django.db.models import Sum

@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_trilla_customer(request):
    try:
        query= TrillaCustomer.objects.all()
        serializer= TrillaCustomerSerializer(query, many= True)
        total_trips = TrillaCustomer.objects.count()
        total_value_rent = TrillaCustomer.objects.aggregate(total_value=Sum('value_rent'))['total_value']
        total_quantity= TrillaCustomer.objects.aggregate(total_quantity=Sum('quantity'))['total_quantity']
        response_data= {'total_trips': total_trips,
                        'total_value_rent': total_value_rent,
                        'total_quantity': total_quantity,
                        'data': serializer.data,
                        }
        return Response(response_data, status= HTTP_200_OK)
    except Exception as error:
        return Response(f'sorry there are problem while getting the data :( : {error})', status= HTTP_400_BAD_REQUEST)