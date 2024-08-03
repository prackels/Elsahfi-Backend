from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from users.models import User
from ...models import Code, EncryptedCodes, EmployeesCodes
from ..serializers import CodeSerializer, EncryptedCodesSerializer, EmployeesCodesSerializer
from django.contrib.auth.hashers import check_password

@api_view(["POST"])
@permission_classes([permissions.IsAdminUser])
def create_encrypted_codes(request):
    try:
        serializer = EncryptedCodesSerializer(data=request.data)
        existing_category = EncryptedCodes.objects.filter(category=request.data.get('category')).exists()
        if existing_category:
            return Response('Please enter another category', status=status.HTTP_400_BAD_REQUEST)
        existing_code = EncryptedCodes.objects.filter(code=request.data.get('code')).exists()
        if existing_code:
            return Response('Please enter another code', status=status.HTTP_400_BAD_REQUEST)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as error:
        return Response(f'An error occurred while processing your request {error}', status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
@permission_classes([permissions.IsAdminUser])
def create_employees_codes(request):
    if request.user.is_superuser:
        user_password = request.user.password
        password = request.data.get('password')
        if password and check_password(password, user_password):
            try:
                serializer = EmployeesCodesSerializer(data=request.data)
                existing_category = EmployeesCodes.objects.filter(category=request.data.get('category')).exists()
                if existing_category:
                    return Response('Please enter another category', status=status.HTTP_400_BAD_REQUEST)
                existing_code = EmployeesCodes.objects.filter(code=request.data.get('code')).exists()
                if existing_code:
                    return Response('Please enter another code', status=status.HTTP_400_BAD_REQUEST)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except Exception as error:
                return Response(f'An error occurred while processing your request {error}', status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response('Invalid password', status=status.HTTP_403_FORBIDDEN)
    else:
        return Response('You are not authorized', status=status.HTTP_403_FORBIDDEN)



@api_view(["POST"])
@permission_classes([permissions.IsAdminUser])
def create_codes(request):
    try:
        serializer = CodeSerializer(data=request.data)
        
        existing_category= Code.objects.filter(category= request.data.get('category'))
        if existing_category:
            return Response('Please enter another category', status= status.HTTP_400_BAD_REQUEST)
        existing_code= Code.objects.filter(code= request.data.get('code'))
        if existing_code:
            return Response('Please enter another code', status= status.HTTP_400_BAD_REQUEST)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except Exception as error:
        return Response(f'An error occurred while processing your request {error}', status=status.HTTP_400_BAD_REQUEST)