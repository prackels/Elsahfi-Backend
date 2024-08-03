import json
from rest_framework.decorators import api_view, permission_classes
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from clients_.models import NewCustomer
from customer_orders.models import DeiannaCustomer, TrillaCustomer, CustomerStation
from cash_station.models import PaymentOfTheDeadLine, Cash
from customer_orders.apis.serializers import DeiannaCustomerSerializer, TrillaCustomerSerializer, CustomerStationSerializer
from django.db.models import Sum, F

@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_customer_report(request, customer):
    try:
            try:
                customer_instance= NewCustomer.objects.get(customer_name= customer)
            except NewCustomer.DoesNotExist as error:
                return Response(f'sorry client not found :( error: {error}')
            customer_data = PaymentOfTheDeadLine.objects.filter(customer_name=customer_instance).aggregate(
            payment_amount=Sum('payment_amount'),
            )
            try:
                the_amount_required_and_financial_advance = Cash.objects.get(customer= customer_instance)
            except Exception as error:
                return Response('no data found about this client :(', status= HTTP_400_BAD_REQUEST)
            if customer_data['payment_amount'] is None:
                customer_data['payment_amount'] = 0

            financial_advance =the_amount_required_and_financial_advance.financial_advance 
            the_amount_required = the_amount_required_and_financial_advance.the_amount_required
            payment_amount_1= customer_data.get('payment_amount')
            financial_advance= the_amount_required_and_financial_advance.financial_advance
            the_amount_required= the_amount_required_and_financial_advance.the_amount_required
#######################################################################################################################################
                                    ### Rent ###
            deianna_customer_total_rent= DeiannaCustomer.objects.filter(customer_name= customer_instance).aggregate(
                rent= Sum('value_rent'),
            )
            if deianna_customer_total_rent['rent'] is None:
                deianna_customer_total_rent['rent'] = 0

            trilla_customer_total_rent= TrillaCustomer.objects.filter(customer_name= customer_instance).aggregate(
                rent= Sum('value_rent'),
            )
            if trilla_customer_total_rent['rent'] is None:
                trilla_customer_total_rent['rent'] = 0
                
            deianna_rent= deianna_customer_total_rent.get('rent')
            trilla_rent= trilla_customer_total_rent.get('rent')
            total_rent= (deianna_rent + trilla_rent)
#######################################################################################################################################
                                        ### All Orders Data ###
            deianna_customer_orders= DeiannaCustomer.objects.filter(customer_name= customer_instance)
            deianna_customer_orders_serializer= DeiannaCustomerSerializer(deianna_customer_orders, many= True)

            trilla_customer_orders= TrillaCustomer.objects.filter(customer_name= customer_instance)
            trilla_customer_orders_serializer= TrillaCustomerSerializer(trilla_customer_orders, many= True)

            customer_station_orders= CustomerStation.objects.filter(customer_name= customer_instance)
            customer_station_orders_serializer= CustomerStationSerializer(customer_station_orders, many= True)

            customer_orders= [deianna_customer_orders_serializer.data, trilla_customer_orders_serializer.data, customer_station_orders_serializer.data]
#######################################################################################################################################
                                        ### Get Gasoline Data For Deianna ###
            deianna_91= DeiannaCustomer.objects.filter(customer_name= customer_instance, subject_name= 'Premium Gasoline 91').aggregate(
                quantity= Sum(F('secret_counter')),
                total= Sum(F('secret_counter') * F('price_per_litre'))
            )
            deianna_total_orders_91= DeiannaCustomer.objects.filter(customer_name= customer_instance, subject_name= 'Premium Gasoline 91').count()

            if deianna_91['quantity'] is None:
                deianna_91['quantity'] = 0

            if deianna_91['total'] is None:
                deianna_91['total'] = 0

            deianna_95= DeiannaCustomer.objects.filter(customer_name= customer_instance, subject_name= 'Premium Gasoline 95').aggregate(
                quantity= Sum(F('secret_counter')),
                total= Sum(F('secret_counter') * F('price_per_litre'))
            )
            deianna_total_orders_95= DeiannaCustomer.objects.filter(customer_name= customer_instance, subject_name= 'Premium Gasoline 95').count()

            if deianna_95['quantity'] is None:
                deianna_95['quantity'] = 0

            if deianna_95['total'] is None:
                deianna_95['total'] = 0

            deianna_diesel= DeiannaCustomer.objects.filter(customer_name= customer_instance, subject_name= 'Diesel').aggregate(
                quantity= Sum(F('secret_counter')),
                total= Sum(F('secret_counter') * F('price_per_litre'))
            )
            deianna_total_orders_diesel= DeiannaCustomer.objects.filter(customer_name= customer_instance, subject_name= 'Diesel').count()

            if deianna_diesel['quantity'] is None:
                deianna_diesel['quantity'] = 0

            if deianna_diesel['total'] is None:
                deianna_diesel['total'] = 0

#######################################################################################################################################
                                        ### Get Gasoline Data For Trilla ###
            trilla_91= TrillaCustomer.objects.filter(customer_name= customer_instance, subject_name= 'Premium Gasoline 91').aggregate(
                quantity= Sum(F('secret_counter')),
                total= Sum(F('secret_counter') * F('price_per_litre'))
            )
            trilla_total_orders_91= TrillaCustomer.objects.filter(customer_name= customer_instance, subject_name= 'Premium Gasoline 91').count()

            if trilla_91['quantity'] is None:
                trilla_91['quantity'] = 0

            if trilla_91['total'] is None:
                trilla_91['total'] = 0

            trilla_95= TrillaCustomer.objects.filter(customer_name= customer_instance, subject_name= 'Premium Gasoline 95').aggregate(
                quantity= Sum(F('secret_counter')),
                total= Sum(F('secret_counter') * F('price_per_litre'))
            )
            trilla_total_orders_95= TrillaCustomer.objects.filter(customer_name= customer_instance, subject_name= 'Premium Gasoline 95').count()


            if trilla_95['quantity'] is None:
                trilla_95['quantity'] = 0

            if trilla_95['total'] is None:
                trilla_95['total'] = 0

            trilla_diesel= TrillaCustomer.objects.filter(customer_name= customer_instance, subject_name= 'Diesel').aggregate(
                quantity= Sum(F('secret_counter')),
                total= Sum(F('secret_counter') * F('price_per_litre'))
            )
            trilla_total_orders_diesel= TrillaCustomer.objects.filter(customer_name= customer_instance, subject_name= 'Diesel').count()
            
            if trilla_diesel['quantity'] is None:
                trilla_diesel['quantity'] = 0
            if trilla_diesel['total'] is None:
                trilla_diesel['total'] = 0
            
#######################################################################################################################################
                                        ### Get Gasoline Data For Customer ###
            customer_91= CustomerStation.objects.filter(customer_name= customer_instance, subject_name= 'Premium Gasoline 91').aggregate(
                quantity_= Sum(F('quantity')),
                total= Sum(F('quantity') * F('price_per_litre'))
            )
            customer_total_orders_91= CustomerStation.objects.filter(customer_name= customer_instance, subject_name= 'Premium Gasoline 91').count()

            if customer_91['quantity_'] is None:
                customer_91['quantity_'] = 0
            if customer_91['total'] is None:
                customer_91['total'] = 0

            customer_95= CustomerStation.objects.filter(customer_name= customer_instance, subject_name= 'Premium Gasoline 95').aggregate(
                quantity_= Sum(F('quantity')),
                total= Sum(F('quantity') * F('price_per_litre'))
            )
            customer_total_orders_95= CustomerStation.objects.filter(customer_name= customer_instance, subject_name= 'Premium Gasoline 95').count()
            if customer_95['quantity_'] is None:
                customer_95['quantity_'] = 0
            if customer_95['total'] is None:
                customer_95['total'] = 0

            customer_diesel= CustomerStation.objects.filter(customer_name= customer_instance, subject_name= 'Diesel').aggregate(
                quantity_= Sum(F('quantity')),
                total= Sum(F('quantity') * F('price_per_litre'))
            )
            customer_total_orders_diesel= CustomerStation.objects.filter(customer_name= customer_instance, subject_name= 'Diesel').count()
            
            if customer_diesel['quantity_'] is None:
                customer_diesel['quantity_'] = 0
            if customer_diesel['total'] is None:
                customer_diesel['total'] = 0

#######################################################################################################################################
                                        ### Count all Gasoline ###
            total_orders_count_premium_gasoline_91= (deianna_total_orders_91 + trilla_total_orders_91 + customer_total_orders_91)
            total_quantity_premium_gasoline_91= (deianna_91.get('secret_counter', 0) + trilla_91.get('secret_counter', 0) + customer_91.get('quantity', 0))
            total_gasoline_91= (deianna_91.get('total', 0) + trilla_91.get('total', 0) + customer_91.get('total', 0))

            total_orders_count_premium_gasoline_95= (deianna_total_orders_95 + trilla_total_orders_95 + customer_total_orders_95)
            total_quantity_premium_gasoline_95= (deianna_95.get('secret_counter', 0) + trilla_95.get('secret_counter', 0) + customer_95.get('quantity', 0))
            total_gasoline_95= (deianna_95.get('total', 0) + trilla_95.get('total', 0) + customer_95.get('total', 0))

            total_orders_count_diesel= (deianna_total_orders_diesel + trilla_total_orders_diesel + customer_total_orders_diesel)
            total_quantity_diesel= (deianna_diesel.get('secret_counter', 0) + trilla_diesel.get('secret_counter', 0) + customer_diesel.get('quantity', 0))
            total_diesel= (deianna_diesel.get('total', 0) + trilla_diesel.get('total', 0) + customer_diesel.get('total', 0))
            
#######################################################################################################################################
            ### Total ###
            total= ((total_quantity_premium_gasoline_91 + total_quantity_premium_gasoline_95 + total_quantity_diesel) * (total_gasoline_91 + total_gasoline_95 + total_diesel))
#######################################################################################################################################
            merged_data = list(zip(deianna_customer_orders_serializer.data, trilla_customer_orders_serializer.data, customer_station_orders_serializer.data))

            json_response = json.dumps(merged_data)

            data= {
                ### Customer Details ###
                'financial_advance': financial_advance,
                'the_amount_required': the_amount_required,
                'payment_amount': payment_amount_1,
                'the_remaining_amount_is_paid': the_amount_required,
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

                ### Total & Total Rent
                'total_rent': total_rent,
                'total': total,
                ### Orders ###
                'customer_orders': customer_orders,
                'deianna_customer_serializer': deianna_customer_orders_serializer.data,
                'trilla_customer_serializer': trilla_customer_orders_serializer.data,
                'customer_station_serializer': customer_station_orders_serializer.data,
            }
            return Response(data, status= HTTP_200_OK)
    except Exception as error:
        return Response({"message": f"an error occurred: {error}"}, status=HTTP_400_BAD_REQUEST)