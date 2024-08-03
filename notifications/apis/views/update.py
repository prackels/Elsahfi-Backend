from rest_framework import decorators,permissions, status
from rest_framework.response import Response
from ...serializers import NotificationSerializer
from ...models import Notification

@decorators.permission_classes([permissions.IsAdminUser])
@decorators.api_view(["PUT",])
def read_notification(request, noti_id):
    try:
        notification = Notification.objects.get(pk=noti_id)
    except Notification.DoesNotExist:
        return Response({
            "message": "Notification not found"
        }, status=status.HTTP_404_NOT_FOUND)
    
    try:
        notification.read = True
        notification.save()
        return Response({
            "message": "Notification read successfully!"
        }, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response({
            "message": "Couldn't get all the notifications"
        }, status=status.HTTP_400_BAD_REQUEST)