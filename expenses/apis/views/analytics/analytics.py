from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from ....models import CarsExpenses, GovernmentExpense, StationExpense
from clients_.models import NewCustomer

@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_expenses_analytics(request):
    try:
        total_station_expenses = StationExpense.objects.count()
        total_government_expenses = GovernmentExpense.objects.count()
        total_car_expenses = CarsExpenses.objects.count()
        total_records = total_station_expenses + total_government_expenses + total_car_expenses

        percentage_station_expenses = (total_station_expenses / total_records) * 100 if total_records != 0 else 0
        percentage_government_expenses = (total_government_expenses / total_records) * 100 if total_records != 0 else 0
        percentage_car_expenses = (total_car_expenses / total_records) * 100 if total_records != 0 else 0

        data = {
            "station_expenses": f"{percentage_station_expenses:.2f}",
            "government_expenses": f"{percentage_government_expenses:.2f}",
            "car_expenses": f"{percentage_car_expenses:.2f}",
            "total_expenses": total_records
        }
        
        return Response(data, status= HTTP_200_OK)
    except Exception as error:
        return Response(f'Sorry, there was a problem while getting the data: {error}', status= HTTP_400_BAD_REQUEST)
