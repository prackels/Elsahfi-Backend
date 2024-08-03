from rest_framework import decorators,permissions, status
from rest_framework.response import Response
from ...serializers import TrillaCustomersSerializer
from ....models import TrillaCustomers

@decorators.api_view(['GET'])
@decorators.permission_classes([permissions.IsAdminUser])
def get_trilla_customers(request):
    try:
        query= TrillaCustomers.objects.all()
        serializer= TrillaCustomersSerializer(query, many= True)
        return Response(serializer.data, status= status.HTTP_200_OK)
    except Exception as error:
        return Response({"message" : f"an error accured : {error}"}, status=status.HTTP_400_BAD_REQUEST)