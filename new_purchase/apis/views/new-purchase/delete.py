from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from django.db.models import F
from tank.models import Tank
from ....models import NewPurchase
from rest_framework.response import Response

@api_view(['DELETE'])
@permission_classes([permissions.IsAdminUser])
def delete_new_purchase(request, pk):
    try:
        query= NewPurchase.objects.get(sequence=pk)
        try:
            tank = Tank.objects.filter(material= query.subject_name).last()
            if tank:
                tank.tank_quantity -= float(query.actual_quantity)
                tank.save()
            query.delete()
        except Exception as error:
            return Response({"message" : f"an error occurred : {error}"}, status=status.HTTP_400_BAD_REQUEST)
        return Response('deleted :)', status= status.HTTP_200_OK)
    except NewPurchase.DoesNotExist:
        return Response('sorry model not found :(', status= status.HTTP_404_NOT_FOUND)