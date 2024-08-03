from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from ....models import NewSupplier
from rest_framework.response import Response

@api_view(['DELETE'])
@permission_classes([permissions.IsAdminUser])
def delete_new_supplier(request, pk):
    try:
        query= NewSupplier.objects.get(sequence=pk)
        try:
            query.delete()
        except Exception as error:
            return Response({"message" : f"an error accured : {error}"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(status= status.HTTP_200_OK)
    except NewSupplier.DoesNotExist:
        return Response('sorry model not found:(', status= status.HTTP_404_NOT_FOUND)