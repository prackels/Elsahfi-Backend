from rest_framework.decorators import api_view, permission_classes
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from clients_.models import NewCustomer
from customer_orders.models import DeiannaCustomer, TrillaCustomer, CustomerStation
from cash_station.models import PaymentOfTheDeadLine
from customer_orders.apis.serializers import DeiannaCustomerSerializer, TrillaCustomerSerializer, CustomerStationSerializer
from django.db.models import Sum
from django.db.models import F

def get_customer_report( customer):

    customer_instance= NewCustomer.objects.filter(customer_name= customer)
    customer_data= PaymentOfTheDeadLine.objects.filter(customer_name= customer_instance).aggregate(
        financial_advance= 'financial_advance',
        the_amount_required= Sum('the_amount_required'),
        # payment_amount= Sum(),
        # the_amount_required= ,
    )
    
    deianna_customer= DeiannaCustomer.objects.filter(customer_name= customer_instance, payment_method= 'debit')
    deianna_customer_serializer= DeiannaCustomerSerializer(deianna_customer, many= True)

    trilla_customer= TrillaCustomer.objects.filter(customer_name= customer_instance, payment_method= 'debit')
    trilla_customer_serializer= TrillaCustomerSerializer(trilla_customer, many= True)

    customer_station= CustomerStation.objects.filter(customer_name= customer_instance, payment_method= 'debit')
    customer_station_serializer= CustomerStationSerializer(customer_station, many= True)

#######################################################################################################################################
    deianna_91= DeiannaCustomer.objects.filter(client= customer_instance, subject_name= 'Premium Gasoline 91').aggregate(
        quantity= Sum('quantity'),
        total= Sum(F('quantity') * F('price_per_litre'))
    )
    deianna_total_orders_91= DeiannaCustomer.objects.filter(client= customer_instance, subject_name= 'Premium Gasoline 91').count()


    deianna_95= DeiannaCustomer.objects.filter(client= customer_instance, subject_name= 'Premium Gasoline 95').aggregate(
        quantity= Sum('quantity'),
        total= Sum(F('quantity') * F('price_per_litre'))
    )
    deianna_total_orders_95= DeiannaCustomer.objects.filter(client= customer_instance, subject_name= 'Premium Gasoline 95').count()


    deianna_diesel= DeiannaCustomer.objects.filter(client= customer_instance, subject_name= 'Diesel').aggregate(
        quantity= Sum('quantity'),
        total= Sum(F('quantity') * F('price_per_litre'))
    )
    deianna_total_orders_diesel= DeiannaCustomer.objects.filter(client= customer_instance, subject_name= 'Diesel').count()
#######################################################################################################################################
    trilla_91= TrillaCustomer.objects.filter(client= customer_instance, subject_name= 'Premium Gasoline 91').aggregate(
        quantity= Sum('secret_counter'),
        total= Sum(F('secret_counter') * F('price_per_litre'))
    )
    trilla_total_orders_91= TrillaCustomer.objects.filter(client= customer_instance, subject_name= 'Premium Gasoline 91').count()


    trilla_95= TrillaCustomer.objects.filter(client= customer_instance, subject_name= 'Premium Gasoline 95').aggregate(
        quantity= Sum('secret_counter'),
        total= Sum(F('secret_counter') * F('price_per_litre'))
    )
    trilla_total_orders_95= TrillaCustomer.objects.filter(client= customer_instance, subject_name= 'Premium Gasoline 95').count()


    trilla_diesel= TrillaCustomer.objects.filter(client= customer_instance, subject_name= 'Diesel').aggregate(
        quantity= Sum('secret_counter'),
        total= Sum(F('secret_counter') * F('price_per_litre'))
    )
    trilla_total_orders_diesel= TrillaCustomer.objects.filter(client= customer_instance, subject_name= 'Diesel').count()
#######################################################################################################################################
    customer_91= CustomerStation.objects.filter(client= customer_instance, subject_name= 'Premium Gasoline 91').aggregate(
        quantity= Sum('secret_counter'),
        total= Sum(F('secret_counter') * F('price_per_litre'))
    )
    customer_total_orders_91= CustomerStation.objects.filter(client= customer_instance, subject_name= 'Premium Gasoline 91').count()


    customer_95= CustomerStation.objects.filter(client= customer_instance, subject_name= 'Premium Gasoline 95').aggregate(
        quantity= Sum('secret_counter'),
        total= Sum(F('secret_counter') * F('price_per_litre'))
    )
    customer_total_orders_95= CustomerStation.objects.filter(client= customer_instance, subject_name= 'Premium Gasoline 95').count()


    customer_diesel= CustomerStation.objects.filter(client= customer_instance, subject_name= 'Diesel').aggregate(
        quantity= Sum('secret_counter'),
        total= Sum(F('secret_counter') * F('price_per_litre'))
    )
    customer_total_orders_diesel= CustomerStation.objects.filter(client= customer_instance, subject_name= 'Diesel').count()
#######################################################################################################################################

    total_orders_count_premium_gasoline_91= (deianna_total_orders_91 + trilla_total_orders_91 + customer_total_orders_91)
    total_quantity_premium_gasoline_91= (deianna_91.get['quantity'] + trilla_91.get['quantity'] + customer_91.get['quantity'])
    total_gasoline_91= (deianna_91.get['total'] + trilla_91.get['total'] + customer_91.get['total'])

    total_orders_count_premium_gasoline_95= (deianna_total_orders_95 + trilla_total_orders_95 + customer_total_orders_95)
    total_quantity_premium_gasoline_95= (deianna_95.get['quantity'] + trilla_95.get['quantity'] + customer_95.get['quantity'])
    total_gasoline_95= (deianna_95.get['total'] + trilla_95.get['total'] + customer_95.get['total'])

    total_orders_count_diesel= (deianna_total_orders_diesel + trilla_total_orders_diesel + customer_total_orders_diesel)
    total_quantity_diesel= (deianna_diesel.get['quantity'] + trilla_diesel.get['quantity'] + customer_diesel.get['quantity'])
    total_diesel= (deianna_diesel.get['total'] + trilla_diesel.get['total'] + customer_diesel.get['total'])

    data= {
        
        ### Gasoline ###
        'total_orders_count_premium_gasoline_91': total_orders_count_premium_gasoline_91,
        'total_quantity_premium_gasoline_91': total_quantity_premium_gasoline_91,
        'total_gasoline_91': total_gasoline_91,

        'total_orders_count_premium_gasoline_95': total_orders_count_premium_gasoline_95,
        'total_quantity_premium_gasoline_95': total_quantity_premium_gasoline_95,
        'total_gasoline_95': total_gasoline_95,

        'total_orders_count_diesel' : total_orders_count_diesel,
        'total_quantity_diesel': total_quantity_diesel,
        'total_diesel': total_diesel,

        ### Orders ###
        'deianna_customer_serializer': deianna_customer_serializer,
        'trilla_customer_serializer': trilla_customer_serializer,
        'customer_station_serializer': customer_station_serializer,
    }
    return data
    # return Response(data, status= HTTP_400_BAD_REQUEST)
