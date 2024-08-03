from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from ....models import CustomerStation, TrillaCustomer, DeiannaCustomer
from clients_.models import NewCustomer
@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_clients_analytics(request):
    try:
        total_records_station = CustomerStation.objects.count()
        total_records_trilla = TrillaCustomer.objects.count()
        total_records_deianna = DeiannaCustomer.objects.count()
        total_records_blocked= NewCustomer.objects.filter(blocked= True).count()
        total_records_pending= NewCustomer.objects.filter(pending= True).count()

        total_records = total_records_station + total_records_trilla + total_records_deianna + total_records_blocked + total_records_pending
        
        percentage_station = (total_records_station / total_records) * 100 if total_records != 0 else 0
        percentage_trilla = (total_records_trilla / total_records) * 100 if total_records != 0 else 0
        percentage_deianna = (total_records_deianna / total_records) * 100 if total_records != 0 else 0
        percentage_blocked= (total_records_blocked / total_records) * 100 if total_records != 0 else 0
        percentage_pending= (total_records_pending / total_records) * 100 if total_records != 0 else 0
        data = {
            "customer_station": f"{percentage_station:.2f}",
            "trilla_customer": f"{percentage_trilla:.2f}",
            "deianna_customer": f"{percentage_deianna:.2f}",
            "blocked_clients": f"{percentage_blocked:.2f}",
            "pending_clients": f"{percentage_pending:.2f}",
            "total_customers": total_records
        }
        return Response(data, HTTP_200_OK)
    except Exception as error:
        print(error)
        return Response('Sorry, there was a problem while getting the data: {error}')
