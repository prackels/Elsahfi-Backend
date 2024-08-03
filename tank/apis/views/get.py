from decimal import Decimal
from rest_framework import status, decorators, permissions
from rest_framework.response import Response
from tank.apis.serializer import TankSerializer, Tank
from trumpet.models import ReadingTrumpet, Trumpet
from shift.models import Shift
from django.db.models import Sum, F
@decorators.api_view(['GET'])
@decorators.permission_classes([permissions.IsAdminUser])
def GetTanks (request):
    try:
        queryset = Tank.objects.all()
        serializer = TankSerializer(queryset,many=True)
        count= queryset.count()
        data= {
            'tank_count': count,
            'data': serializer.data
        }
        return Response(data,status=status.HTTP_200_OK)
    except Exception as error :
        return Response({
            'message' : f'an error occurred : {error}'
        },status=status.HTTP_400_BAD_REQUEST)



@decorators.api_view(['GET'])
@decorators.permission_classes([permissions.IsAdminUser])
def get_tanks_details(request):
    try:
        shift = Shift.objects.filter(is_active= False).last()

        tank_91 = Tank.objects.filter(material='Premium Gasoline 91').last()
        quantity_91 = tank_91.tank_quantity if tank_91 else 0
        caliber_91 = tank_91.tank_caliber if tank_91 else 0
        sold_91 = ReadingTrumpet.objects.filter(shift=shift).aggregate(
            total_quantity_sold=Sum('quantity_sold')
        )
        total_quantity_sold_91 = sold_91['total_quantity_sold'] if sold_91['total_quantity_sold'] else 0
        trumpets_91_count = Trumpet.objects.filter(subject_name='Premium Gasoline 91').count()

        #########################################
        tank_95 = Tank.objects.filter(material='Premium Gasoline 95').last()
        quantity_95 = tank_95.tank_quantity if tank_95 else 0
        caliber_95 = tank_95.tank_caliber if tank_95 else 0
        sold_95 = ReadingTrumpet.objects.filter(shift=shift, subject_name= 'Premium Gasoline 95').aggregate(
            total_quantity_sold=Sum('quantity_sold')
        )
        total_quantity_sold_95 = sold_95['total_quantity_sold'] if sold_95['total_quantity_sold'] else 0
        trumpets_95_count = Trumpet.objects.filter(subject_name='Premium Gasoline 95').count()
        #########################################
        tank_diesel = Tank.objects.filter(material='Diesel').last()
        quantity_diesel = tank_diesel.tank_quantity if tank_diesel else 0
        caliber_diesel = tank_diesel.tank_caliber if tank_diesel else 0

        sold_diesel = ReadingTrumpet.objects.filter(shift=shift, subject_name= 'Diesel').aggregate(
            total_quantity_sold=Sum('quantity_sold')
        )
        total_quantity_sold_diesel = sold_diesel['total_quantity_sold'] if sold_diesel['total_quantity_sold'] else 0
        trumpets_diesel_count = Trumpet.objects.filter(subject_name='Diesel').count()


        data = {
            'quantity_91': round(quantity_91),
            'caliber_91': round(caliber_91),
            'sold_91': round(total_quantity_sold_91),
            'trumpets_91_count': trumpets_91_count,
            
            'quantity_95': round(quantity_95),
            'caliber_95': round(caliber_95),
            'sold_95': round(total_quantity_sold_95),
            'trumpets_95_count': trumpets_95_count,

            'quantity_diesel': round(quantity_diesel),
            'caliber_diesel': round(caliber_diesel),
            'sold_diesel': round(total_quantity_sold_diesel),
            'trumpets_diesel_count': trumpets_diesel_count,
        }
        return Response(data, status=status.HTTP_200_OK)
    except Exception as error:
        return Response({'message': f'an error occurred: {error}'}, status=status.HTTP_400_BAD_REQUEST)