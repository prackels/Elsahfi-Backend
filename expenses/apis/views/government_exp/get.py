from rest_framework import decorators,permissions, status
from rest_framework.response import Response
from expenses.apis.serializers import GovernmentExpSerializer
from expenses.models import GovernmentExpense
from django.db.models import Sum

@decorators.api_view(['GET'])
@decorators.permission_classes([permissions.IsAdminUser])
def get_gov_station_expenses (request) : 
    try :
        queryset = GovernmentExpense.objects.all()
        serializer = GovernmentExpSerializer(queryset,many=True)
        totals = GovernmentExpense.objects.aggregate(
            total_cost_of_license=Sum('cost_of_license'),
            total_employee_insurance=Sum('employee_insurance'),
            total_car_insurance=Sum('car_insurance'),
            total_renwal_of_form=Sum('renwal_of_form'),
        )
        
        data = {
            'total_exp': totals,
            'data': serializer.data
        }
        return Response(data,status=status.HTTP_200_OK)
    except Exception as error:
        return Response({
            'message' : f'an error accured : {error}'
        },status=status.HTTP_400_BAD_REQUEST)