from rest_framework import decorators,permissions, status
from rest_framework.response import Response
from ...serializers import DepositCashToTheStationSerializer
from ....models import DepositCashToTheStation

@decorators.api_view(['GET'])
@decorators.permission_classes([permissions.IsAdminUser])
def get_deposit_cash_to_the_station(request):
    try:
        query= DepositCashToTheStation.objects.all()
        serializer= DepositCashToTheStationSerializer(query, many= True)
        return Response(serializer.data, status= status.HTTP_200_OK)
    except Exception as error : 
        return Response({"message" : f"an error accured : {error}"}, status=status.HTTP_400_BAD_REQUEST)