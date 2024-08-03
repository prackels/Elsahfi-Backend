from celery import shared_task
from time import sleep
from .models import Shift

@shared_task
def close_shift_automatically():
    
    current_shift = Shift.objects.last()
    sleep_for_6_Hours = ( 60 * 60) * 6

    sleep(sleep_for_6_Hours)

    current_shift.is_active = False
    current_shift.save()

