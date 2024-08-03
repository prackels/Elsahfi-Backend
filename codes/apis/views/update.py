from rest_framework import decorators, status, permissions
from rest_framework.response import Response
from ...models import Code, EncryptedCodes
from ..serializers import CodeSerializer, EncryptedCodesSerializer
from users.models import User
from django.contrib.auth.hashers import check_password

@decorators.api_view(["PUT"])
@decorators.permission_classes([permissions.IsAdminUser])
def update_encrypted_codes(request, pk):
    try:
        query = EncryptedCodes.objects.get(pk=pk)
        serializer = EncryptedCodesSerializer(query, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except EncryptedCodes.DoesNotExist:
        return Response({"message": "EncryptedCodes not found"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"message": f"An error occurred while updating the codes: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

# @decorators.api_view(['PUT'])
# @decorators.permission_classes([permissions.IsAdminUser])
# def update_employees_codes(request, pk):
#     try:
#         query= EncryptedCodes.objects.get(pk= pk)
#         serializer= EncryptedCodesSerializer(query,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status= status.HTTP_200_OK)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#     except Exception:
#         return Response({"message": "an error occurred while updating the codes"}, status=status.HTTP_400_BAD_REQUEST)


@decorators.api_view(['PUT'])
@decorators.permission_classes([permissions.IsAdminUser])
def update_codes(request, pk): 
    try:
        try:
            query = Code.objects.get(sequence= pk)
            serializer = CodeSerializer(query, request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response({"message": "an error occurred while updating the codes"}, status=status.HTTP_400_BAD_REQUEST)
    except Exception:
        return Response({"message": "an error occurred while updating the codes"}, status=status.HTTP_400_BAD_REQUEST)