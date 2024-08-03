from rest_framework.decorators import api_view, permission_classes
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from invoices.models import *

@api_view(['GET'])
@permission_classes([IsAdminUser])
def invoices_count(request):
    try:
        shift_instance= Shift.objects.filter(is_active= False).last()
        if shift_instance:
            station_customer_invoice= StationCustomerInvoice.objects.filter(shift=shift_instance).count()
            trilla_customers= TrillaCustomers.objects.filter(shift= shift_instance).count()
            new_purchasing_clients_invoice= NewPurchasingClientsInvoice.objects.filter(shift= shift_instance).count()
            deianna_customer_invoice= DeiannaCustomerInvoice.objects.filter(shift= shift_instance).count()
            station_expense_invoice= StationExpenseInvoice.objects.filter(shift= shift_instance).count()
            government_expenses_invoice= GovernmentExpensesInvoice.objects.filter(shift= shift_instance).count()
            official_papers_of_employees_invoice= OfficialPapersOfEmployeesInvoice.objects.filter(shift= shift_instance).count()
            deposit_cash_to_the_station= DepositCashToTheStation.objects.filter(shift= shift_instance).count()
            total_count= station_customer_invoice + trilla_customers + new_purchasing_clients_invoice + deianna_customer_invoice + station_expense_invoice + government_expenses_invoice + official_papers_of_employees_invoice + deposit_cash_to_the_station
            return Response({'invoices_count': total_count}, status= HTTP_200_OK)
        else:
            return Response('sorry no shift data :(', status= HTTP_400_BAD_REQUEST)
    except Exception as error:
        return Response({'message' : f'an error occurred : {error}'}, status=HTTP_400_BAD_REQUEST)