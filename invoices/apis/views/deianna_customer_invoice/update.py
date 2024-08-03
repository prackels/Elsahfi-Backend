from rest_framework import decorators, status, permissions
from rest_framework.response import Response
from ....models import DeiannaCustomerInvoice
from ...serializers import DeiannaCustomerInvoiceSerializer


@decorators.api_view(['PUT'])
@decorators.permission_classes([permissions.IsAdminUser])
def update_deianna_customer_invoice (request, pk) : 
    try:
        try:
            query = DeiannaCustomerInvoice.objects.get(sequance=pk)
        except DeiannaCustomerInvoice.DoesNotExist:
                return Response('sorry this invoice not found', status=status.HTTP_404_NOT_FOUND)
        serializer = DeiannaCustomerInvoiceSerializer(query, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as error : 
        return Response({"message" : f"an error accured : {error}"}, status=status.HTTP_400_BAD_REQUEST)