from django.urls import path
from .apis.views.customer import create
from .apis.views.customer import blocked_pending
from .apis.views.customer import delete
from .apis.views.customer import update
from .apis.views.cars import get as get_cars, create as create_cars, update as update_car, delete as delete_car
from .apis.views.subjects import create as create_subject, delete as delete_subject, get as get_subjects, update as update_subjects
from .apis.views.customer import get

urlpatterns = [
    path('customer/create/', create.create_new_customer),
    path('customer/get/', get.get_new_customer),
    path('customer/get-byname/<str:customer_name>/', get.get_new_customer_byname),
    path('customer/pending/get/', get.get_pending_customers),
    path('customer/blocked/get/', get.get_blocked_customers),
    path('customer/update/<int:pk>/', update.update_new_customer),
    path('customer/delete/<int:pk>/', delete.delete_new_customer),

    path('car/get/', get_cars.get_cars),
    path('car/get-all/', get_cars.get_all_cars),
    path('car/get-for/<str:customer_name>/', get_cars.get_customer_cars),
    path('car/create/', create_cars.create_car_for_the_client),
    path('car/update/<int:pk>/', update_car.update_client_car),
    path('car/delete/<int:pk>/', delete_car.delete_customer_car),

    path('subject/get/', get_subjects.get_subjects),
    path('subject/get-all/', get_subjects.get_all_subjects),
    path('subject/create/', create_subject.create_subject_for_the_client),
    path('subject/update/<int:pk>/', update_subjects.update_client_subject),
    path('subject/delete/<int:pk>/', delete_subject.delete_customer_subject),

    path('new-customer/block/<int:pk>/', blocked_pending.block_customer),
    path('new-customer/unblock/<int:pk>/', blocked_pending.unblock_customer),
    path('new-customer/pend/<int:pk>/', blocked_pending.pend_customer),
    path('new-customer/unpend/<int:pk>/', blocked_pending.unpend_customer),
]