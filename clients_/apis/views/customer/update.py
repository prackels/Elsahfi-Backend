from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from ....models import NewCustomer
from ...serializers import NewCustomerSerializer

@api_view(['PUT'])
@permission_classes([IsAdminUser])
def update_new_customer(request, pk):
    try:
        customer= NewCustomer.objects.get(sequence= pk)
        customer_serializer= NewCustomerSerializer(customer, data= request.data)
        if customer_serializer.is_valid():
            customer_serializer.save()
        else:
            return Response({'message': 'Please correct your customer data :(', 'errors': customer_serializer.errors}, status= HTTP_400_BAD_REQUEST)
        return Response(customer_serializer.data, status= HTTP_200_OK)
    except Exception as error:
        return Response({'message' : f'an error occurred : {error}'}, status= HTTP_400_BAD_REQUEST)