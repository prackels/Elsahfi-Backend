from rest_framework import decorators,permissions, status
from rest_framework.response import Response
from ...serializers import NewPurchasingClientsInvoiceSerializer
from ....models import NewPurchasingClientsInvoice

@decorators.api_view(['GET'])
@decorators.permission_classes([permissions.IsAdminUser])
def get_new_purchasing_clients_invoice(request):
    try:
        query= NewPurchasingClientsInvoice.objects.all()
        serializer= NewPurchasingClientsInvoiceSerializer(query, many= True)
        return Response(serializer.data, status= status.HTTP_200_OK)
    except Exception as error:
        return Response({"message" : f"an error accured : {error}"}, status=status.HTTP_400_BAD_REQUEST)