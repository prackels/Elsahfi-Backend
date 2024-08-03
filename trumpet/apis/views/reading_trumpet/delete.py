from rest_framework import permissions, status
from rest_framework.decorators import permission_classes, api_view
from rest_framework.response import Response

from tank.models import Tank
from ....models import ReadingTrumpet, ReadingTrumpet_K

@api_view(['DELETE'])
@permission_classes([permissions.IsAdminUser])
def delete_reading_trumpet(request, pk):
    try:
        query = ReadingTrumpet.objects.get(id=pk)
    except ReadingTrumpet.DoesNotExist:
        return Response('This model not found :()', status=status.HTTP_404_NOT_FOUND)
    try:
        tank = Tank.objects.filter(material= query.subject_name).last()
        if tank:
                tank.tank_quantity += float(query.quantity_sold)
                tank.save()
        query.delete()
        return Response('DELETED :)', status=status.HTTP_200_OK)
    except Exception as error:
        return Response(f'Sorry, there was an error: {error}', status=status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE'])
@permission_classes([permissions.IsAdminUser])
def delete_reading_trumpet_k(request, pk):
    try:
        query = ReadingTrumpet_K.objects.get(id=pk)
    except ReadingTrumpet_K.DoesNotExist:
        return Response('This model not found :(', status=status.HTTP_404_NOT_FOUND)
    try:
        tank = Tank.objects.filter(material= query.subject_name).last()
        if tank:
                tank.tank_quantity += float(query.quantity_sold)
                tank.save()
        query.delete()
        return Response('DELETED :)', status=status.HTTP_200_OK)
    except Exception as error:
        return Response(f'Sorry, there was an error: {error}', status=status.HTTP_400_BAD_REQUEST)