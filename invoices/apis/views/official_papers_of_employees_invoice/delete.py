from rest_framework import decorators
from ....models import OfficialPapersOfEmployeesInvoice
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status

@decorators.api_view(['DELETE'])
@decorators.permission_classes([permissions.IsAdminUser])
def delete_official_papers_of_employees_invoice(request, pk):
    try:
        query= OfficialPapersOfEmployeesInvoice.objects.get(sequance= pk)
        try:
            query.delete()
        except Exception as error:
            return Response({"message" : f"an error accured : {error}"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(status= status.HTTP_200_OK)
    except OfficialPapersOfEmployeesInvoice.DoesNotExist:
        return Response('sorry model not found', status= status.HTTP_404_NOT_FOUND)