from rest_framework import decorators
from ....models import NewCustomer
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status

@decorators.api_view(['DELETE'])
@decorators.permission_classes([permissions.IsAdminUser])
def delete_new_customer(request, pk):
    try:
        query= NewCustomer.objects.get(sequence= pk)
        try:
            query.delete()
        except Exception as error:
            return Response({"message" : f"an error accured : {error}"}, status=status.HTTP_400_BAD_REQUEST)
        return Response('deleted successfully :)', status= status.HTTP_200_OK)
    except NewCustomer.DoesNotExist:
        return Response('sorry ur request not found :()', status= status.HTTP_404_NOT_FOUND)