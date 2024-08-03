from rest_framework import decorators,permissions, status
from rest_framework.response import Response
from ...serializers import NotificationSerializer
from ...models import Notification

@decorators.permission_classes([permissions.IsAdminUser])
@decorators.api_view(["GET",])
def get_all_notifications(request):
    user = request.user
    try:
        notifications = Notification.objects.filter(to_user=user).order_by("sent_at")
    except Exception as e:
        print(e)
        return Response({
            "message": "Couldn't get all the notifications"
        }, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        serializer = NotificationSerializer(notifications, many=True)
        return Response({
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response({
            "message": "Couldn't get all the notifications"
        }, status=status.HTTP_400_BAD_REQUEST)