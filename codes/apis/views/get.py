from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from users.models import User
from ...models import Code, EncryptedCodes
from ..serializers import CodeSerializer, EncryptedCodesSerializer

@api_view(['POST', 'GET'])
@permission_classes([permissions.IsAdminUser])
def get_encrypted_codes(request, codes_type):
    try:
        main_admin = User.objects.filter(is_superuser=True).first()
    except Exception as e:
        return Response({
            "message": "Couldn't find the main admin"
        }, status=status.HTTP_400_BAD_REQUEST)
    password = request.data.get("password")
    try:
        if main_admin.check_password(password):
            try:
                codes = EncryptedCodes.objects.filter(type=codes_type).order_by("-added_at")
                serializer = EncryptedCodesSerializer(codes, many= True)
                return Response(serializer.data, status= status.HTTP_200_OK)
            except Exception as e:
                return Response({"message": "an error occurred while getting the codes"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "an error occurred while getting the codes, please insert password field"}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"message": "The password that you provided isn't correct"}, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['GET'])
@permission_classes([permissions.IsAdminUser])
def get_codes(request):
    try:
        codes= Code.objects.all().order_by("added_at")
        serializer= CodeSerializer(codes, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)
    except Exception as error:
        return Response({"message": f"an error occurred while getting the codes: {error}"}, status= status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
@permission_classes([permissions.IsAdminUser])
def get_encrypted_employee_codes(request):
    try:
        codes= EncryptedCodes.objects.filter(type="Employee").order_by("added_at")
        serializer= CodeSerializer(codes, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)
    except Exception as error:
        return Response({"message": f"an error occurred while getting the codes: {error}"}, status= status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([permissions.IsAdminUser])
def get_encrypted_private_codes(request):
    try:
        codes= EncryptedCodes.objects.filter(type="Private").order_by("added_at")
        serializer= CodeSerializer(codes, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)
    except Exception as error:
        return Response({"message": f"an error occurred while getting the codes: {error}"}, status= status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET",])
@permission_classes([permissions.IsAdminUser])
def get_codes_by(request, code):
    try:
        codes = Code.objects.filter(code=code).order_by("added_at")
        serializer= CodeSerializer(codes, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)
    except Exception as error:
        return Response({"message": f"an error occurred while getting the codes: {error}"}, status= status.HTTP_400_BAD_REQUEST)