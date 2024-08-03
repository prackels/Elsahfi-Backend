from rest_framework.decorators import api_view, permission_classes
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from employee.models import Car
from employee.apis.serializers import CarSerializer
from expenses.models import CarsExpenses
from expenses.apis.serializers import CarsExpensesSerializer
from customer_orders.models import DeiannaCustomer, TrillaCustomer
from customer_orders.apis.serializers import DeiannaCustomerSerializer, TrillaCustomerSerializer
from django.db.models import Sum
from django.db.models import F


def get_car_report(car):
    car_instance= Car.objects.get(car_name= car)
    car_expenses = CarsExpenses.objects.filter(car_type= car_instance).aggregate(
        total_exp=Sum('total_price')
    )
    car_expenses_details= CarsExpenses.objects.filter(car_type=car_instance)
    car_expenses_details_serializer= CarsExpensesSerializer(car_expenses_details, many= True)

    deianna = DeiannaCustomer.objects.filter(car_type= car_instance)
    deianna_serializer= DeiannaCustomerSerializer(deianna, many=True)

    trilla = TrillaCustomer.objects.filter(car_type= car_instance)
    trilla_serializer= TrillaCustomerSerializer(trilla, many= True)

    deianna_data = DeiannaCustomer.objects.filter(car_type=car_instance).aggregate(
        total_rent=Sum('value_rent'),
        total_price=Sum(F('quantity') * F('price_per_litre')),
        total_trip=Sum((F('quantity') * F('price_per_litre')) + F('value_rent') - F('tips'))
    )

    trilla_data = TrillaCustomer.objects.filter(car_type=car_instance).aggregate(
        total_rent=Sum('value_rent'),
        total_price=Sum(F('quantity') * F('price_per_litre')),
        total_trip=Sum((F('quantity') * F('price_per_litre')) + F('value_rent') - F('tips'))
    )
    
    if car_expenses['total_exp'] is None:
        car_expenses['total_exp'] = 0
    if deianna_data['total_rent'] is None:
        deianna_data['total_rent'] = 0
    if deianna_data['total_price'] is None:
        deianna_data['total_price'] = 0
    if deianna_data['total_trip'] is None:
        deianna_data['total_trip'] = 0
    if trilla_data['total_rent'] is None:
        trilla_data['total_rent'] = 0
    if trilla_data['total_price'] is None:
        trilla_data['total_price'] = 0
    if trilla_data['total_trip'] is None:
        trilla_data['total_trip'] = 0
    
    trips = deianna.count() + trilla.count()
    total_rent = deianna_data.get('total_rent') + trilla_data.get('total_rent')
    total_trips = deianna_data.get('total_trip') + trilla_data.get('total_trip')
    total_expenses = car_expenses.get('total_exp')
    final_profits = (total_trips - total_expenses)

    data = {
        'trips': trips,
        'total_rent': total_rent,
        'total_trips': total_trips,
        'total_expenses': total_expenses,
        'final_profits': final_profits,
        'car_expenses_details': car_expenses_details_serializer.data,
        'customers_orders': {'deianna': deianna_serializer.data,
                            'trilla': trilla_serializer.data
                            }
            }
    return data
    # return Response(data, status=HTTP_200_OK)
