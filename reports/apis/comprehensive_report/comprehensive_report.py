from decimal import Decimal
from rest_framework.decorators import api_view, permission_classes
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from shift.models import Shift
from shift.apis.serializers import ShiftSerializer
from expenses.models import CarsExpenses, StationExpense, GovernmentExpense
from new_purchase.models import NewPurchase, NewSupplier
from customer_orders.models import DeiannaCustomer, TrillaCustomer, CustomerStation
from django.db.models import Sum, F
from employee.models import Car
from cash_station.models import ShiftCash
from invoices.models import *
from invoices.apis.serializers import *
from datetime import datetime
from django.utils import timezone

@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_comprehensive_report(request, from_date, to_date):
    try:
###################################################################################################################################################
            ### Total Expenses ###
            station_exp= StationExpense.objects.filter(date__range=(from_date, to_date)).aggregate(
                total_exp= Sum(F('total_price'))
            )
            gov_exp= GovernmentExpense.objects.filter(date__range=(from_date, to_date)).aggregate(
                total_exp= Sum(F('employee_insurance') + F('car_insurance') + F('renwal_of_form') + F('cost_of_license'))
            )
            car_exp= CarsExpenses.objects.filter(date__range=(from_date, to_date)).aggregate(
                total_exp= Sum(F('total_price'))
            )
            purchase_data= NewPurchase.objects.filter(date__range=(from_date, to_date)).aggregate(
                price_quantity= Sum((F('quantity_received')) * (F('price_per_litre')))
            )
            if station_exp['total_exp'] is None:
                station_exp['total_exp'] = 0
                
            if gov_exp['total_exp'] is None:
                gov_exp['total_exp'] = 0

            if car_exp['total_exp'] is None:
                car_exp['total_exp'] = 0

            if purchase_data['price_quantity'] is None:
                purchase_data['price_quantity'] = 0

            total_exp_= (station_exp.get('total_exp') + gov_exp.get('total_exp') + car_exp.get('total_exp') + purchase_data.get('price_quantity'))
###################################################################################################################################################
            ### Purchase Taxes ###
            try:
                purchase_tax_value = NewSupplier.objects.filter(date__range=(from_date, to_date), supplier_name= 'ارامكو').last().purchase_tax
            except AttributeError:
                purchase_tax_value = 0

            all_purchase= NewPurchase.objects.filter(date__range=(from_date, to_date), supplier_name__supplier_name= purchase_tax_value).aggregate(
                total_quantity_received_per_liter= Sum((F('quantity_received') * (F('price_per_litre')))),
            )
            if all_purchase['total_quantity_received_per_liter'] is None:
                all_purchase['total_quantity_received_per_liter']= 0

            all_purchase_data = Decimal(all_purchase.get('total_quantity_received_per_liter'))
            purchase_tax_value = Decimal(purchase_tax_value)
            total_purchase_taxes = (purchase_tax_value / Decimal(100)) * all_purchase_data
###################################################################################################################################################
            ### Total Sales ###
            deianna_purchase= DeiannaCustomer.objects.filter(date__range=(from_date, to_date)).aggregate(
                total= Sum(F('price_per_litre') * F('secret_counter'))
            )
            trilla_purchase= TrillaCustomer.objects.filter(date__range=(from_date, to_date)).aggregate(
                total= Sum(F('price_per_litre') * F('secret_counter'))
            )
            customer_purchase= CustomerStation.objects.filter(date__range=(from_date, to_date)).aggregate(
                total= Sum(F('price_per_litre') * F('quantity'))
            )
            if deianna_purchase['total'] is None:
                deianna_purchase['total']= 0

            if trilla_purchase['total'] is None:
                trilla_purchase['total']= 0

            if customer_purchase['total'] is None:
                customer_purchase['total']= 0

            toatl_customers_sales= (deianna_purchase.get('total') + trilla_purchase.get('total') + customer_purchase.get('total'))
###################################################################################################################################################
            ### Sales Taxes ###
            quantity_received_91= NewPurchase.objects.filter(date__range=(from_date, to_date), subject_name= 'Premium Gasoline 91').aggregate(
                total_received_quantity= Sum(F('quantity_received'))
            )
            quantity_received_95= NewPurchase.objects.filter(date__range=(from_date, to_date), subject_name= 'Premium Gasoline 95').aggregate(
                total_received_quantity= Sum(F('quantity_received'))
            )
            quantity_received_diesel= NewPurchase.objects.filter(date__range=(from_date, to_date), subject_name= 'Diesel').aggregate(
                total_received_quantity= Sum(F('quantity_received'))
            )
            if quantity_received_91['total_received_quantity'] is None:
                quantity_received_91['total_received_quantity']= 0

            if quantity_received_95['total_received_quantity'] is None:
                quantity_received_95['total_received_quantity']= 0

            if quantity_received_diesel['total_received_quantity'] is None:
                quantity_received_diesel['total_received_quantity']= 0
                

            new_supplier = NewSupplier.objects.last()
            liter_selling_price_91 =  0 if new_supplier is None else new_supplier.liter_selling_price_91
            liter_selling_price_95 = 0 if new_supplier is None else new_supplier.liter_selling_price_95
            liter_selling_price_diesel = 0 if new_supplier is None else new_supplier.liter_selling_price_diesel
            sales_tax_value = new_supplier.sales_tax or 0 if new_supplier else 0

            sales_tax_value = Decimal(sales_tax_value)

            total_sales_per_price= ((quantity_received_91.get('total_received_quantity') * liter_selling_price_91) + (quantity_received_95.get('total_received_quantity') * liter_selling_price_95) + (quantity_received_diesel.get('total_received_quantity') * liter_selling_price_diesel))
            total_sales_per_price= Decimal(total_sales_per_price)
            total_sales_taxes= (sales_tax_value / Decimal(100) * total_sales_per_price)
###################################################################################################################################################
            ### Net Profit ###
            sales_without_a_taxes= (Decimal(toatl_customers_sales) - Decimal(total_sales_taxes))
            total_net_profit= (Decimal(sales_without_a_taxes) - Decimal(total_exp_))
###################################################################################################################################################
            ### Expenses details ###
            purchase_91= NewPurchase.objects.filter(date__range=(from_date, to_date), subject_name= 'Premium Gasoline 91').aggregate(
                actual_quantity_total= Sum(F('actual_quantity')),
                the_amount_of_evaporation_total= Sum(F('the_amount_of_evaporation')),
                the_difference_per_quantity_total= Sum(F('the_difference_per_quantity')),
                total_purchase= Sum(F('price_per_litre') * F('quantity_received')),
                the_amount_of_evaporation_total_per_price= Sum(F('price_per_litre') * F('the_amount_of_evaporation')),
                the_difference_per_quantity_total_per_price= Sum(F('price_per_litre') * F('the_difference_per_quantity')),
            )
            purchase_91_price_per_liter = 0
            purchase_91_price_per_liter_value = NewPurchase.objects.filter(date__range=(from_date, to_date), subject_name='Premium Gasoline 91').last()
            if purchase_91_price_per_liter_value:
                purchase_91_price_per_liter = purchase_91_price_per_liter_value.price_per_litre
            purchase_95= NewPurchase.objects.filter(date__range=(from_date, to_date), subject_name= 'Premium Gasoline 95').aggregate(
                actual_quantity_total= Sum(F('actual_quantity')),
                the_amount_of_evaporation_total= Sum(F('the_amount_of_evaporation')),
                the_difference_per_quantity_total= Sum(F('the_difference_per_quantity')),
                total_purchase= Sum(F('price_per_litre') * F('quantity_received')),
                the_amount_of_evaporation_total_per_price= Sum(F('price_per_litre') * F('the_amount_of_evaporation')),
                the_difference_per_quantity_total_per_price= Sum(F('price_per_litre') * F('the_difference_per_quantity')),
            )
            purchase_95_price_per_liter = 0
            purchase_95_price_per_liter_value = NewPurchase.objects.filter(date__range=(from_date, to_date), subject_name='Premium Gasoline 95').last()
            if purchase_95_price_per_liter_value:
                purchase_95_price_per_liter = purchase_95_price_per_liter_value.price_per_litre

            purchase_diesel= NewPurchase.objects.filter(date__range=(from_date, to_date), subject_name= 'Diesel').aggregate(
                actual_quantity_total= Sum(F('actual_quantity')),
                the_amount_of_evaporation_total= Sum(F('the_amount_of_evaporation')),
                the_difference_per_quantity_total= Sum(F('the_difference_per_quantity')),
                total_purchase= Sum(F('price_per_litre') * F('quantity_received')),
                the_amount_of_evaporation_total_per_price= Sum(F('price_per_litre') * F('the_amount_of_evaporation')),
                the_difference_per_quantity_total_per_price= Sum(F('price_per_litre') * F('the_difference_per_quantity')),
            )
            purchase_diesel_price_per_liter = 0
            purchase_diesel_price_per_liter_value = NewPurchase.objects.filter(date__range=(from_date, to_date), subject_name='Diesel').last()
            if purchase_diesel_price_per_liter_value:
                purchase_diesel_price_per_liter = purchase_diesel_price_per_liter_value.price_per_litre

            if purchase_91['actual_quantity_total'] is None:
                purchase_91['actual_quantity_total'] = 0
            if purchase_91['the_amount_of_evaporation_total'] is None:
                purchase_91['the_amount_of_evaporation_total'] = 0
            if purchase_91['the_difference_per_quantity_total'] is None:
                purchase_91['the_difference_per_quantity_total'] = 0
            if purchase_91['total_purchase'] is None:
                purchase_91['total_purchase'] = 0
            if purchase_91['the_amount_of_evaporation_total_per_price'] is None:
                purchase_91['the_amount_of_evaporation_total_per_price'] = 0
            if purchase_91['the_difference_per_quantity_total_per_price'] is None:
                purchase_91['the_difference_per_quantity_total_per_price'] = 0
            
            if purchase_95['actual_quantity_total'] is None:
                purchase_95['actual_quantity_total'] = 0
            if purchase_95['the_amount_of_evaporation_total'] is None:
                purchase_95['the_amount_of_evaporation_total'] = 0
            if purchase_95['the_difference_per_quantity_total'] is None:
                purchase_95['the_difference_per_quantity_total'] = 0
            if purchase_95['total_purchase'] is None:
                purchase_95['total_purchase'] = 0
            if purchase_95['the_amount_of_evaporation_total_per_price'] is None:
                purchase_95['the_amount_of_evaporation_total_per_price'] = 0
            if purchase_95['the_difference_per_quantity_total_per_price'] is None:
                purchase_95['the_difference_per_quantity_total_per_price'] = 0

            if purchase_diesel['actual_quantity_total'] is None:
                purchase_diesel['actual_quantity_total'] = 0
            if purchase_diesel['the_amount_of_evaporation_total'] is None:
                purchase_diesel['the_amount_of_evaporation_total'] = 0
            if purchase_diesel['the_difference_per_quantity_total'] is None:
                purchase_diesel['the_difference_per_quantity_total'] = 0
            if purchase_diesel['total_purchase'] is None:
                purchase_diesel['total_purchase'] = 0
            if purchase_diesel['the_amount_of_evaporation_total_per_price'] is None:
                purchase_diesel['the_amount_of_evaporation_total_per_price'] = 0
            if purchase_diesel['the_difference_per_quantity_total_per_price'] is None:
                purchase_diesel['the_difference_per_quantity_total_per_price'] = 0
            ################ 
            purchase_91_price_per_liter= purchase_91_price_per_liter
            purchase_91_actual_quantity_total= purchase_91.get('actual_quantity_total')
            purchase_91_the_amount_of_evaporation_total= purchase_91.get('the_amount_of_evaporation_total')
            purchase_91_the_difference_per_quantity_total= purchase_91.get('the_difference_per_quantity_total')
            purchase_91_total_purchase= purchase_91.get('total_purchase')
            purchase_91_the_amount_of_evaporation_total_per_price= purchase_91.get('the_amount_of_evaporation_total_per_price')
            purchase_91_the_difference_per_quantity_total_per_price= purchase_91.get('the_difference_per_quantity_total_per_price')
            ###############
            purchase_95_price_per_liter= purchase_95_price_per_liter
            purchase_95_actual_quantity_total= purchase_95.get('actual_quantity_total')
            purchase_95_the_amount_of_evaporation_total= purchase_95.get('the_amount_of_evaporation_total')
            purchase_95_the_difference_per_quantity_total= purchase_95.get('the_difference_per_quantity_total')
            purchase_95_total_purchase= purchase_95.get('total_purchase')
            purchase_95_the_amount_of_evaporation_total_per_price= purchase_95.get('the_amount_of_evaporation_total_per_price')
            purchase_95_the_difference_per_quantity_total_per_price= purchase_95.get('the_difference_per_quantity_total_per_price')
            ###############
            purchase_diesel_price_per_liter= purchase_diesel_price_per_liter
            purchase_diesel_actual_quantity_total= purchase_diesel.get('actual_quantity_total')
            purchase_diesel_the_amount_of_evaporation_total= purchase_diesel.get('the_amount_of_evaporation_total')
            purchase_diesel_the_difference_per_quantity_total= purchase_diesel.get('the_difference_per_quantity_total')
            purchase_diesel_total_purchase= purchase_diesel.get('total_purchase')
            purchase_diesel_the_amount_of_evaporation_total_per_price= purchase_diesel.get('the_amount_of_evaporation_total_per_price')
            purchase_diesel_the_difference_per_quantity_total_per_price= purchase_diesel.get('the_difference_per_quantity_total_per_price')
#################################################
            station_exp_total= station_exp.get('total_exp')
            gov_exp_total= gov_exp.get('total_exp')
            car_exp_total= car_exp.get('total_exp')
            total_exp_with_taxes= Decimal(total_exp_)
            total_purchase_taxes_total= Decimal(total_purchase_taxes)
            net_expenses= total_exp_with_taxes - total_purchase_taxes_total
###################################################################################################################################################
            ### Sales Details ###
            liter_price_91 = liter_selling_price_91
            if not liter_price_91:
                liter_price_91= 0
            else:
                liter_price_91 = float(liter_price_91)

            liter_price_95= liter_selling_price_95
            if not liter_price_95:
                liter_price_95= 0
            else:
                liter_price_95 = float(liter_price_95)

            liter_price_diesel= liter_selling_price_91
            if not liter_price_diesel:
                liter_price_diesel= 0
            else:
                liter_price_diesel = float(liter_price_diesel)
            
#################################################
## UP ^^ ##
#################################################
            total_purchase_gasoline_91= NewPurchase.objects.filter(date__range=(from_date, to_date), subject_name= 'Premium Gasoline 91').aggregate(
                total_purchases= Sum(F('quantity_received')),
            )
            total_purchase_gasoline_95= NewPurchase.objects.filter(date__range=(from_date, to_date), subject_name= 'Premium Gasoline 95').aggregate(
                total_purchases= Sum(F('quantity_received')),
            )
            total_purchase_gasoline_diesel= NewPurchase.objects.filter(date__range=(from_date, to_date), subject_name= 'Diesel').aggregate(
                total_purchases= Sum(F('quantity_received')),
            )
            
            total_purchase_gasoline_91_per_quantity= float(total_purchase_gasoline_91.get('total_purchases') or 0)
            total_purchase_gasoline_95_per_quantity= float(total_purchase_gasoline_95.get('total_purchases') or 0)
            total_purchase_gasoline_diesel_per_quantity= float(total_purchase_gasoline_diesel.get('total_purchases') or 0)
#################################################
            total_quantity_sold_91_= ((total_purchase_gasoline_91_per_quantity) * (liter_price_91))
            total_quantity_sold_95_= ((total_purchase_gasoline_95_per_quantity) * (liter_price_95))
            total_quantity_sold_diesel_= ((total_purchase_gasoline_diesel_per_quantity) * (liter_price_diesel))
#################################################
            total_quantity_with_taxes= total_quantity_sold_91_ + total_quantity_sold_95_ + total_quantity_sold_diesel_
#################################################
            required_sales_taxes= total_sales_taxes
###################################################################################################################################################
            ### Imports Of Station Cars ###
            cars_data = []
            cars = Car.objects.all()
            for car in cars:
                deianna_cars = DeiannaCustomer.objects.filter(car_type=car, date__range=(from_date, to_date))
                trilla_cars = TrillaCustomer.objects.filter(car_type=car, date__range=(from_date, to_date))

                total_deianna_trips = deianna_cars.aggregate(total_trips=Sum('total_trip'))
                total_deianna_trips = total_deianna_trips['total_trips'] if total_deianna_trips['total_trips'] is not None else 0

                total_deianna_rent = deianna_cars.aggregate(total_rent=Sum('value_rent'))
                total_deianna_rent = total_deianna_rent['total_rent'] if total_deianna_rent['total_rent'] is not None else 0

                total_trilla_trips = trilla_cars.aggregate(total_trips=Sum('total_trip'))
                total_trilla_trips = total_trilla_trips['total_trips'] if total_trilla_trips['total_trips'] is not None else 0

                total_trilla_rent = trilla_cars.aggregate(total_rent=Sum('value_rent'))
                total_trilla_rent = total_trilla_rent['total_rent'] if total_trilla_rent['total_rent'] is not None else 0


                total_trips = total_deianna_trips + total_trilla_trips
                total_rent = total_deianna_rent + total_trilla_rent
                total_trips_count = deianna_cars.count() + trilla_cars.count()
                cars_data.append({
                    'car_name': car.car_name,
                    'total_trips': total_trips,
                    'total_rent': total_rent,
                    'total_trips_count': total_trips_count,
                })
###################################################################################################################################################
            ### Taxes ###
            sales_taxes = StationExpense.objects.filter(expense_code__code='01',date__range=(from_date, to_date)).aggregate(
                total_paid=Sum(F('total_price')) or 0
            )
            required_purchase_taxes = total_purchase_taxes
            paid_purchase_taxes = total_purchase_taxes
            purchase_taxes_remaining = 0
            #######################################
            required_sales_taxes_ = Decimal(total_sales_taxes)
            paid_sales_taxes = Decimal(sales_taxes.get('total_paid', 0)) if sales_taxes.get('total_paid') is not None else Decimal(0)

            sales_remaining_texas = (required_sales_taxes_ - paid_sales_taxes)

###################################################################################################################################################
            ### Invoices and Official Papers ###
            station_customer_invoices = StationCustomerInvoice.objects.filter(date__range=(from_date, to_date))
            trilla_customers = TrillaCustomers.objects.filter(date__range=(from_date, to_date))
            new_purchasing_clients_invoices = NewPurchasingClientsInvoice.objects.filter(date__range=(from_date, to_date))
            deianna_customer_invoices = DeiannaCustomerInvoice.objects.filter(date__range=(from_date, to_date))
            station_expense_invoices = StationExpenseInvoice.objects.filter(date__range=(from_date, to_date))
            government_expenses_invoices = GovernmentExpensesInvoice.objects.filter(date__range=(from_date, to_date))
            official_papers_of_employees_invoices = OfficialPapersOfEmployeesInvoice.objects.filter(date__range=(from_date, to_date))
            deposit_cash_to_the_station = DepositCashToTheStation.objects.filter(date__range=(from_date, to_date))
            
            station_customer_invoices_serializer = StationCustomerInvoiceSerializer(station_customer_invoices, many=True).data
            trilla_customers_serializer = TrillaCustomersSerializer(trilla_customers, many=True).data
            new_purchasing_clients_invoices_serializer = NewPurchasingClientsInvoiceSerializer(new_purchasing_clients_invoices, many=True).data
            deianna_customer_invoices_serializer = DeiannaCustomerInvoiceSerializer(deianna_customer_invoices, many=True).data
            station_expense_invoices_serializer = StationExpenseInvoiceSerializer(station_expense_invoices, many=True).data
            government_expenses_invoices_serializer = GovernmentExpensesInvoiceSerializer(government_expenses_invoices, many=True).data
            official_papers_of_employees_invoices_serializer = OfficialPapersOfEmployeesInvoiceSerializer(official_papers_of_employees_invoices, many=True).data
            deposit_cash_to_the_station_serializer = DepositCashToTheStationSerializer(deposit_cash_to_the_station, many=True).data
            total_invoices_sum= station_customer_invoices.count() + trilla_customers.count() + new_purchasing_clients_invoices.count() + deianna_customer_invoices.count() + station_expense_invoices.count() + government_expenses_invoices.count() + official_papers_of_employees_invoices.count() + deposit_cash_to_the_station.count()
###################################################################################################################################################
            data= {
                'total_exp': round(total_exp_),
                'total_purchase_taxes': round(total_purchase_taxes),
                'toatl_customers_sales': round(toatl_customers_sales),
                'total_sales_taxes': round(total_sales_taxes),
                'net_profit': round(total_net_profit),
                ##################
                'purchase_91_price_per_liter': round(purchase_91_price_per_liter),
                'purchase_91_actual_quantity_total': round(purchase_91_actual_quantity_total),
                'purchase_91_the_amount_of_evaporation_total': round(purchase_91_the_amount_of_evaporation_total),
                'purchase_91_the_difference_per_quantity_total': round(purchase_91_the_difference_per_quantity_total),
                'purchase_91_total_purchase': round(purchase_91_total_purchase),
                'purchase_91_the_amount_of_evaporation_total_per_price': round(purchase_91_the_amount_of_evaporation_total_per_price),
                'purchase_91_the_difference_per_quantity_total_per_price': round(purchase_91_the_difference_per_quantity_total_per_price),
                ###################
                'purchase_95_price_per_liter': round(purchase_95_price_per_liter),
                'purchase_95_actual_quantity_total': round(purchase_95_actual_quantity_total),
                'purchase_95_the_amount_of_evaporation_total': round(purchase_95_the_amount_of_evaporation_total),
                'purchase_95_the_difference_per_quantity_total': round(purchase_95_the_difference_per_quantity_total),
                'purchase_95_total_purchase': round(purchase_95_total_purchase),
                'purchase_95_the_amount_of_evaporation_total_per_price': round(purchase_95_the_amount_of_evaporation_total_per_price),
                'purchase_95_the_difference_per_quantity_total_per_price': round(purchase_95_the_difference_per_quantity_total_per_price),
                ###################
                'purchase_diesel_price_per_liter': round(purchase_diesel_price_per_liter),
                'purchase_diesel_actual_quantity_total': round(purchase_diesel_actual_quantity_total),
                'purchase_diesel_the_amount_of_evaporation_total': round(purchase_diesel_the_amount_of_evaporation_total),
                'purchase_diesel_the_difference_per_quantity_total': round(purchase_diesel_the_difference_per_quantity_total),
                'purchase_diesel_total_purchase': round(purchase_diesel_total_purchase),
                'purchase_diesel_the_amount_of_evaporation_total_per_price': round(purchase_diesel_the_amount_of_evaporation_total_per_price),
                'purchase_diesel_the_difference_per_quantity_total_per_price': round(purchase_diesel_the_difference_per_quantity_total_per_price),
                ###################
                'station_exp_total': round(station_exp_total),
                'gov_exp_total': round(gov_exp_total),
                'car_exp_total': round(car_exp_total),
                'total_exp_with_taxes': round(total_exp_with_taxes),
                'total_purchase_taxes_total': round(total_purchase_taxes_total),
                'net_expenses': round(net_expenses),
                ###################
                'liter_price_91': round(liter_price_91),
                'liter_price_95': round(liter_price_95),
                'liter_price_diesel': round(liter_price_diesel),
                ###################
                'quantity_received_91': round(quantity_received_91.get('total_received_quantity')),
                'quantity_received_95': round(quantity_received_95.get('total_received_quantity')),
                'quantity_received_diesel': round(quantity_received_diesel.get('total_received_quantity')),
                ###################
                'total_quantity_with_taxes': round(total_quantity_with_taxes),
                'required_sales_taxes': round(required_sales_taxes),
                ###################
                'cars_data': cars_data,
                ###################
                'total_sales': round(sales_without_a_taxes), # Without taxes
                'net_profits': round(total_net_profit),
                ###################
                'required_purchase_taxes': round(required_purchase_taxes),
                'paid_purchase_taxes': round(paid_purchase_taxes),
                'purchase_taxes_remaining': round(purchase_taxes_remaining),

                'required_sales_taxes_': round(required_sales_taxes_),
                'paid_sales_taxes': round(paid_sales_taxes),
                'sales_remaining_texas': round(sales_remaining_texas),
                ###################
                "station_customer_invoices": station_customer_invoices_serializer,
                "trilla_customers": trilla_customers_serializer,
                "new_purchasing_clients_invoices": new_purchasing_clients_invoices_serializer,
                "deianna_customer_invoices": deianna_customer_invoices_serializer,
                "station_expense_invoices": station_expense_invoices_serializer,
                "government_expenses_invoices": government_expenses_invoices_serializer,
                "official_papers_of_employees_invoices": official_papers_of_employees_invoices_serializer,
                "deposit_cash_to_the_station": deposit_cash_to_the_station_serializer,
                "total_invoices_sum": total_invoices_sum,
            }
            return Response(data, status= HTTP_200_OK)
    except Exception as error:
        return Response({"message": f"an error occurred: {error}"}, status=HTTP_400_BAD_REQUEST)
