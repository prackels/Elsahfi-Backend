from rest_framework.decorators import api_view, permission_classes
from rest_framework import status, permissions
from rest_framework.response import Response

from tank.models import Tank
from ...serializers import ReadingTrumpetSerializer, ReadingTrumpetKSerializer
from ....models import ReadingTrumpet, ReadingTrumpet_K

@api_view(['PUT'])
@permission_classes([permissions.IsAdminUser])
def update_reading_trumpet(request, pk):
    try:
        try:
            query = ReadingTrumpet.objects.get(id=pk)
            old_quantity = query.quantity_sold
        except ReadingTrumpet.DoesNotExist:
            return Response('sorry this trumpet not found', status=status.HTTP_404_NOT_FOUND)
        serializer = ReadingTrumpetSerializer(query, request.data)
        new_quantity = float(request.data.get('quantity_sold'))
        quantity_difference = new_quantity - old_quantity

        tank = Tank.objects.filter(material= request.data['subject_name']).last()
        if tank:
            tank.tank_quantity -= quantity_difference
            tank.save()
            
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as error:
        return Response({"message" : f"an error occurred : {error}"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([permissions.IsAdminUser])
def update_reading_trumpet_k(request, pk):
    try:
        try:
            query = ReadingTrumpet_K.objects.get(id=pk)
            old_quantity = query.quantity_sold
        except ReadingTrumpet_K.DoesNotExist:
            return Response('sorry this trumpet not found', status=status.HTTP_404_NOT_FOUND)
        serializer = ReadingTrumpetKSerializer(query, request.data)
        tank = Tank.objects.filter(material= request.data['subject_name']).last()
        new_quantity = float(request.data.get('quantity_sold'))
        quantity_difference = new_quantity - old_quantity
        if tank:
            tank.tank_quantity -= quantity_difference
            tank.save()
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as error:
        return Response({"message" : f"an error occurred : {error}"}, status=status.HTTP_400_BAD_REQUEST)