from rest_framework import decorators,permissions, status
from rest_framework.response import Response
from ...serializers import DeiannaCustomerInvoiceSerializer
from ....models import DeiannaCustomerInvoice

@decorators.api_view(['GET'])
@decorators.permission_classes([permissions.IsAdminUser])
def get_deianna_customer_invoice(request):
    try:
        query= DeiannaCustomerInvoice.objects.all()
        serializer= DeiannaCustomerInvoiceSerializer(query, many= True)
        return Response(serializer.data, status= status.HTTP_200_OK)
    except Exception as error:
        return Response({"message" : f"an error accured : {error}"}, status=status.HTTP_400_BAD_REQUEST)
    