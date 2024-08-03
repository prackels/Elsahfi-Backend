from rest_framework import decorators,permissions, status
from rest_framework.response import Response
from ...serializers import OfficialPapersOfEmployeesInvoiceSerializer
from ....models import OfficialPapersOfEmployeesInvoice

@decorators.api_view(['GET'])
@decorators.permission_classes([permissions.IsAdminUser])
def get_official_papers_of_employees_invoice(request):
    try:
        query= OfficialPapersOfEmployeesInvoice.objects.all()
        serializer= OfficialPapersOfEmployeesInvoiceSerializer(query, many= True)
        return Response(serializer.data, status= status.HTTP_200_OK)
    except Exception as error:
        return Response({"message" : f"an error accured : {error}"}, status=status.HTTP_400_BAD_REQUEST)