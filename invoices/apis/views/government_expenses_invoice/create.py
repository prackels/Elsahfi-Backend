from rest_framework import decorators,permissions, status
from rest_framework.response import Response
from ...serializers import GovernmentExpensesInvoiceSerializer

@decorators.api_view(['POST'])
@decorators.permission_classes([permissions.IsAdminUser])
def create_government_expenses_invoice(request):
    try:
        serializer = GovernmentExpensesInvoiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except Exception as error:
        return Response({"message" : f"an error accured : {error}"}, status=status.HTTP_400_BAD_REQUEST)