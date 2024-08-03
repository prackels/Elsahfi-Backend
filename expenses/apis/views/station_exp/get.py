from rest_framework import decorators,permissions, status
from rest_framework.response import Response
from expenses.apis.serializers import StationExpSerializer
from expenses.models import StationExpense
from django.db.models import Sum

@decorators.api_view(['GET'])
@decorators.permission_classes([permissions.IsAdminUser])
def get_station_expenses (request) : 
    try :
        queryset = StationExpense.objects.all()
        serializer = StationExpSerializer(queryset,many=True)
        total_exp= StationExpense.objects.aggregate(total= Sum('total_price'))['total']
        data= {
            'total_exp': total_exp,
            'data': serializer.data
        }
        return Response(data,status=status.HTTP_200_OK)
    except Exception as error:
        return Response({
            'message' : f'an error accured : {error}'
        },status=status.HTTP_400_BAD_REQUEST)