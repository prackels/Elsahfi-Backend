from rest_framework import decorators, status, permissions
from rest_framework.response import Response

from tank.models import Tank
from ....models import NewPurchase
from ...serializers import NewPurchaseSerializer

@decorators.api_view(['PUT'])
@decorators.permission_classes([permissions.IsAdminUser])
def update_new_purchase(request, pk): 
    try:
        try:
            query = NewPurchase.objects.get(sequence=pk)
            old_quantity = query.actual_quantity
        except NewPurchase.DoesNotExist:
            return Response('sorry this model not found :(', status=status.HTTP_404_NOT_FOUND)
        serializer = NewPurchaseSerializer(query, request.data)
        new_quantity = float(request.data.get('actual_quantity'))
        quantity_difference = new_quantity - old_quantity
        tank = Tank.objects.filter(material= request.data['subject_name']).last()
        if tank:
            tank.tank_quantity += quantity_difference
            tank.save()
            
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as error:
        return Response({"message" : f"an error accured : {error}"}, status=status.HTTP_400_BAD_REQUEST)