from rest_framework import decorators,permissions, status
from rest_framework.response import Response
from ...serializers import ReadingTrumpetSerializer, ReadingTrumpetKSerializer
from ....models import ReadingTrumpet, ReadingTrumpet_K
from django.db.models import Sum


@decorators.api_view(['GET'])
@decorators.permission_classes([permissions.IsAdminUser])
def get_reading_trumpet(request):
    try:
        query= ReadingTrumpet.objects.all()
        serializer= ReadingTrumpetSerializer(query, many= True)
        total_trumpet= query.count()
        total_receiving_counter= ReadingTrumpet.objects.aggregate(total= Sum('receiving_counter'))
        total_delivery_counter= ReadingTrumpet.objects.aggregate(total= Sum('delivery_counter'))
        total_sold= ReadingTrumpet.objects.aggregate(total= Sum('quantity_sold'))
        
        data= {
            'total_trumpet': total_trumpet,
            'total_receiving_counter': total_receiving_counter,
            'total_delivery_counter': total_delivery_counter,
            'total_sold': total_sold,
            'data': serializer.data
        }
        return Response(data, status= status.HTTP_200_OK)
    except Exception as error:
        return Response({"message" : f"an error accured : {error}"}, status=status.HTTP_400_BAD_REQUEST)
    

@decorators.api_view(['GET'])
@decorators.permission_classes([permissions.IsAdminUser])
def get_reading_trumpet_k(request):
    try:
        query= ReadingTrumpet_K.objects.all()
        serializer= ReadingTrumpetKSerializer(query, many= True)
        total_trumpet= query.count()
        total_receiving_counter= ReadingTrumpet_K.objects.aggregate(total= Sum('receiving_counter'))
        total_delivery_counter= ReadingTrumpet_K.objects.aggregate(total= Sum('delivery_counter'))
        total_sold= ReadingTrumpet_K.objects.aggregate(total= Sum('quantity_sold'))
        
        data= {
            'total_trumpet': total_trumpet,
            'total_receiving_counter': total_receiving_counter,
            'total_delivery_counter': total_delivery_counter,
            'total_sold': total_sold,
            'data': serializer.data
        }
        return Response(data, status= status.HTTP_200_OK)
    except Exception as error:
        return Response({"message" : f"an error accured : {error}"}, status=status.HTTP_400_BAD_REQUEST)