from .models import PaymentOfTheDeadLine
from globals.real_time_activity import SendRealTimeActivity as SendNotification
from celery import shared_task
from datetime import timedelta
from django.utils.timezone import now, timedelta

@shared_task
def check_payments():
    
    all_pays = PaymentOfTheDeadLine.objects.all()

    print('start checking the payments')
    for payment in all_pays : 
        if payment.date_of_payment == now().date() : 
            SendNotification(
                content=f"Today is date to pay invoices contract of employee {payment.customer_name.customer_name} at {payment.date_of_payment}",
                noti_type="aleart"
            )

        if payment.date_of_payment == now().date() + timedelta(days=1) : 
            SendNotification(
                content=f"Tomorrow is date to pay invoices contract of employee {payment.customer_name.customer_name} at {payment.date_of_payment}",
                noti_type="aleart"
            )
