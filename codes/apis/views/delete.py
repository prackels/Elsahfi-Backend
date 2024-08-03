from rest_framework import decorators
from ...models import Code, EncryptedCodes
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from users.models import User

@decorators.api_view(['DELETE', 'POST'])
@decorators.permission_classes([permissions.IsAdminUser])
def delete_encrypted_codes(request, pk):
    try:
        main_admin = User.objects.filter(is_superuser=True).first()
    except Exception as e:
        return Response({"message": "Couldn't find the main admin"}, status=status.HTTP_400_BAD_REQUEST)
    try:
        query= EncryptedCodes.objects.get(sequence= pk)
        try:
            query.delete()
        except Exception as error:
            return Response({"message" : f"an error accured : {error}"}, status=status.HTTP_400_BAD_REQUEST)
        return Response('code deleted successfully :)', status= status.HTTP_200_OK)
    except EncryptedCodes.DoesNotExist:
        return Response('sorry this code not found :()', status= status.HTTP_404_NOT_FOUND)


@decorators.api_view(['DELETE'])
@decorators.permission_classes([permissions.IsAdminUser])
def delete_codes(request, pk):
    try:
        query= Code.objects.get(sequence= pk)
        try:
            query.delete()
        except Exception as error:
            return Response({"message" : f"an error accured : {error}"}, status=status.HTTP_400_BAD_REQUEST)
        return Response('DELETED :)', status= status.HTTP_200_OK)
    except Code.DoesNotExist:
        return Response('sorry this code not found :()', status= status.HTTP_404_NOT_FOUND)


