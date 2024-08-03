from rest_framework import decorators, status, permissions
from rest_framework.response import Response
from ....models import OfficialPapersOfEmployeesInvoice
from ...serializers import OfficialPapersOfEmployeesInvoiceSerializer

@decorators.api_view(['PUT'])
@decorators.permission_classes([permissions.IsAdminUser])
def update_official_papers_of_employees_invoice(request, pk): 
    try:
        try:
            query = OfficialPapersOfEmployeesInvoice.objects.get(sequance=pk)
        except OfficialPapersOfEmployeesInvoice.DoesNotExist:
            return Response('sorry this invoice not found', status=status.HTTP_404_NOT_FOUND)
        serializer = OfficialPapersOfEmployeesInvoiceSerializer(query, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as error:
        return Response({"message" : f"an error accured : {error}"}, status=status.HTTP_400_BAD_REQUEST)