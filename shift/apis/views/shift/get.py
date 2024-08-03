from rest_framework import status, decorators, permissions
from rest_framework.response import Response
from ....models import Shift
from ...serializers import ShiftSerializer
from django.utils.timezone import datetime
from new_purchase.models import NewPurchase
from invoices.models import (StationCustomerInvoice, StationExpenseInvoice, DeiannaCustomerInvoice,
GovernmentExpensesInvoice, NewPurchasingClientsInvoice,TrillaCustomers, DepositCashToTheStation, OfficialPapersOfEmployeesInvoice)



@decorators.api_view(['GET'])
@decorators.permission_classes([permissions.IsAdminUser])
def GetShift (request, shift_uid) : 
    try : 
        try : 
            shift = Shift.objects.get(uid=shift_uid,is_active=True)
        except Shift.DoesNotExist : 
            return Response({
                'message' : 'no shift with this uid'
            },status=status.HTTP_404_NOT_FOUND)
        
        serializer = ShiftSerializer(shift)
        return Response(serializer.data,status=status.HTTP_200_OK)
    

    except Exception as error :
        return Response({
            'message' : f'an error accured : {error}'
        },status=status.HTTP_400_BAD_REQUEST)
    
@decorators.api_view(['GET'])
@decorators.permission_classes([permissions.IsAdminUser])
def get_last_shift_id(request):
    try:
        last_shift = Shift.objects.last()
        return Response({
            "data": last_shift.pk
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            "message": "Couldn't get the last shift ID"
        }, status=status.HTTP_400_BAD_REQUEST)
