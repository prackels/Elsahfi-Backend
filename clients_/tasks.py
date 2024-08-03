from celery import shared_task
from .models import Cars, NewCustomer, Subjects

@shared_task(bind= True)
def SaveCarTask(self, customer_save, cars_data, *args, **kwargs):
    customer_id= NewCustomer.objects.get(pk= customer_save)
    try:
        for car_data in cars_data:
            print(f"Processing car data: {car_data}")
            car_instance = Cars.objects.create(
                customer= customer_id,
                car_code=car_data.get('car_code'),
                car_type=car_data.get('car_type'),
                car_plate=car_data.get('car_plate')
            )
            car_instance.save()
            print('task done')
    except Exception as error:
        print(f"Error saving Cars instance: {error}")

@shared_task(bind= True)
def SaveSubjectTask(self, customer_save, subjects_data, *args, **kwargs):
    customer_id= NewCustomer.objects.get(pk= customer_save)
    try:
        for subject_data in subjects_data:
            print(f"Processing subject data: {subject_data}")
            subject_instance = Subjects.objects.create(
                customer= customer_id,
                subject_name= subject_data.get('subject_name'),
                price_per_liter= subject_data.get('price_per_liter')
            )
            subject_instance.save()
            print('task done')
    except Exception as error:
        print(f"Error saving subjects instance: {error}")