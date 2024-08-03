from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.permissions import IsAdminUser
from ....models import TrillaCustomer
from ...serializers import TrillaCustomerSerializer
from django.core.exceptions import ObjectDoesNotExist

@api_view(['PUT'])
@permission_classes([IsAdminUser])
def update_trilla_customer(request, pk):
    try:
        try:
            query= TrillaCustomer.objects.get(sequence= pk)
            serializer= TrillaCustomerSerializer(query, request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status= HTTP_200_OK)
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        except Exception as error:
                return Response(f'there are error: {error}', status= HTTP_400_BAD_REQUEST)
    except ObjectDoesNotExist:
        return Response('sorry ur request not found :( )', status= HTTP_400_BAD_REQUEST)