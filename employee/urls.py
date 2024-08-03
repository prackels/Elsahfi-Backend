from django.urls import path
from .apis.views.employee import (
    get as get_emp,
    update as update_emp,
    delete as delete_emp,
    create as create_emp,
)

from .apis.views.car import (
    get as get_car,
    update as update_car,
    delete as delete_car,
    create as create_car,
)

urlpatterns = [
    
    # employee urls
    path('get/',get_emp.get_employee),
    path('get-byname/<str:employee_name>/',get_emp.get_employee_byname),
    path('create/',create_emp.create_employee),
    path('update/<int:employeeid>/',update_emp.update_employee),
    path('delete/<int:employeeid>/',delete_emp.delete_employee),

    # car urls
    path('car/get/',get_car.get_cars),
    path('car/get-bytype/<str:car_type>/',get_car.get_cars_bytype),
    path('car/create/',create_car.create_car),
    path('car/update/<str:carcode>/',update_car.update_car),
    path('car/delete/<str:carcode>/',delete_car.delete_car),

]