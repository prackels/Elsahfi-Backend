from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from clients_.models import NewCustomer
from ...serializers import NewCustomerSerializer
from rest_framework. status import HTTP_400_BAD_REQUEST, HTTP_200_OK

@api_view(['POST'])
@permission_classes([IsAdminUser])
def create_new_customer(request):
        try:
            customer_serializer = NewCustomerSerializer(data= request.data)
            existing_customer = NewCustomer.objects.filter(customer_name= request.data.get('customer_name'))
            if existing_customer:
                return Response({'error': 'Customer with the same name already exists'}, status=HTTP_400_BAD_REQUEST)
            else:
                customer_serializer = NewCustomerSerializer(data= request.data)
                if customer_serializer.is_valid():
                    customer_serializer.save()
                else:
                    return Response('please correct ur data :(', status= HTTP_400_BAD_REQUEST)
                return Response(customer_serializer.data, status= HTTP_200_OK)
        except Exception as error:
            return Response(f'There is an error: {error}', status= HTTP_400_BAD_REQUEST)