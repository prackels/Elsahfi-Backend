from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()

NOTI_TYPE = (
    ('aleart','aleart'),
    ('receive','receive'),
    ('block','block'),
    ('unblock','unblock'),
)

class Notification (models.Model) : 
    to_user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='to_user_noti')
    from_user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='from_user_noti',null=True,blank=True)
    content = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    type = models.CharField(choices=NOTI_TYPE,max_length=100,null=True,blank=True)

    def __str__ (self) : 
        return f'{self.to_user}'
