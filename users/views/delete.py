from rest_framework import decorators, permissions, status
from rest_framework.response import Response
from ..models import User

@decorators.api_view(["DELETE",])
@decorators.permission_classes([permissions.IsAdminUser])
def delete_user(request, email):
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return Response({
            "message": "No user matches this email"
        }, status=status.HTTP_404_NOT_FOUND)
    
    try:
        user.delete()
        return Response({
            "message": "User deleted successfully"
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            "message": "An error occurred while deleting the user"
        }, status=status.HTTP_400_BAD_REQUEST)