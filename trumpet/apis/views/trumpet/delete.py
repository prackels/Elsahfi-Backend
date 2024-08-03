from rest_framework import decorators
from ....models import Trumpet
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status

@decorators.api_view(['DELETE'])
@decorators.permission_classes([permissions.IsAdminUser])
def delete_trumpet(request, pk):
    try:
        query= Trumpet.objects.get(sequence=pk)
        try:
            query.delete()
        except Exception as error:
            return Response({"message" : f"an error accrued : {error}"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(status= status.HTTP_200_OK)
    except Trumpet.DoesNotExist:
        return Response('sorry model not found', status= status.HTTP_404_NOT_FOUND)
