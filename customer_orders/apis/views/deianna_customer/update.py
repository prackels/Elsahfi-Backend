from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.permissions import IsAdminUser
from ....models import DeiannaCustomer
from ...serializers import DeiannaCustomerSerializer
from django.core.exceptions import ObjectDoesNotExist

@api_view(['PUT'])
@permission_classes([IsAdminUser])
def update_deianna_customer(request, pk):
    try:
        try:
            query= DeiannaCustomer.objects.get(sequence= pk)
            serializer= DeiannaCustomerSerializer(query, request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status= HTTP_200_OK)
        except Exception as error:
                return Response(f'there are error: {error}', status= HTTP_400_BAD_REQUEST)
    except ObjectDoesNotExist:
        return Response('sorry ur request not found :( )', status= HTTP_400_BAD_REQUEST)
        