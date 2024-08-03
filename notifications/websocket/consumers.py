from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from users.models import User
import json
from notifications.models import Notification
from ..serializers import NotificationSerializer

class NotificationConsumer (WebsocketConsumer) : 

    def connect(self):
        
        self.user = self.scope['user']

        
        if self.user.is_anonymous:
            self.close()
            return
        


        self.GROUPNAME = f"notification-{self.user.id}"

        self.accept()

        async_to_sync(self.channel_layer.group_add)(
            self.GROUPNAME,self.channel_name
        )
        

        self.users_notifications = Notification.objects.filter(to_user=self.user)
        serializer = NotificationSerializer(
            self.users_notifications.order_by('sent_at'),
            many=True
        )

        self.data = {
            'data' : serializer.data,
            'un_read' : self.users_notifications.filter(read=False).count()
        }

        self.send(text_data=json.dumps(self.data))



    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            self.GROUPNAME,
            self.channel_name
        )

    def receive(self, text_data):
        json_data = json.loads(text_data)
        
        read = json_data.get('read',False)

        
        if read :
            self.users_notifications.update(read=True)
    
            serializer = NotificationSerializer(
                self.users_notifications.order_by('sent_at'),
                many=True
            )

            self.data = {
                'data' : serializer.data,
                'un_read' : self.users_notifications.filter(read=False).count()
            }
            self.send(text_data=json.dumps(self.data))
            return
        
        to_user_id = json_data['to_user_id']
        content = json_data['content']

        try :
            self.to_user = User.objects.get(id=to_user_id)
        except User.DoesNotExist :
            self.close()
            return
        
        if self.to_user == self.user :
            self.close()
            return

        # create model
        noti = Notification.objects.create(
            from_user = self.user,
            to_user = self.to_user,
            content = content
        )

        noti.save()

        

        async_to_sync(self.channel_layer.group_send)(
            self.GROUPNAME,
            {
                'type' : 'send_notification',
                'message' : NotificationSerializer(noti).data
                
            }
        )

    def send_notification (self,event) :
        self.send(text_data=json.dumps({'message':event['message']}))