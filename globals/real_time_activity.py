from channels.layers import get_channel_layer
from notifications.models import Notification
from users.models import User
from asgiref.sync import async_to_sync
import threading

class SendRealTimeActivity :
    
    def __init__(self, content, from_user=None,noti_type=None) :
        self.content = content
        self.from_user = from_user
        self.noti_type = noti_type
        t = threading.Thread(target=self.send)
        t.start()        

    def send(self) : 
        if self.from_user is None :
            admin_users = User.objects.filter(is_superuser=True)
        else:
            admin_users = User.objects.filter(is_superuser=True).exclude(id=self.from_user.id)
        
        for to_user in admin_users :

             
            noti = Notification.objects.create(
                from_user = self.from_user,
                content = self.content,
                to_user = to_user,
            )

            if self.noti_type is not None : 
                noti.type = self.noti_type

            noti.save()

            channel_layer = get_channel_layer()

            message = {
                "content" : self.content,
                'from_user' : self.from_user.full_name if self.from_user else None,
                'type' : str(self.noti_type) if self.noti_type else None,
            }
            
            async_to_sync(channel_layer.group_send)(
                f"notification-{to_user.id}",
                {
                    'type':"send_notification",
                    'message' : message
                }
            )





