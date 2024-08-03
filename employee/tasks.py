from .models import Employee
from globals.real_time_activity import SendRealTimeActivity as SendNotification
from celery import shared_task
from datetime import timedelta
from django.utils.timezone import now

@shared_task
def check_employees():
    
    all_employees = Employee.objects.all()

    print('start checking')
    for employee in all_employees : 
        if employee.end_of_the_employment_contract == now().date() : 
            SendNotification(
                content=f"Today is date to renew contract of employee {employee.name} at {employee.end_of_the_employment_contract}",
                noti_type="aleart"
            )

