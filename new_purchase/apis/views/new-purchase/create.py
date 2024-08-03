from decimal import Decimal
from rest_framework import decorators, status, permissions
from ...serializers import NewPurchaseSerializer
from ....models import NewSupplier
from rest_framework.response import Response
from tank.models import Tank
from django.db.models import F

@decorators.api_view(['POST'])
@decorators.permission_classes([permissions.IsAdminUser])
def create_new_purchase(request):
    data = request.data.copy()
    try:
        supplier = NewSupplier.objects.get(supplier_name=data.get("supplier_name"))
    except NewSupplier.DoesNotExist:
        return Response({
            "message": "Supplier doesn't exists"
        }, status=status.HTTP_404_NOT_FOUND)
    try : 
        data["supplier_name"] = supplier.pk
        serializer = NewPurchaseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            tank = Tank.objects.filter(material= request.data['subject_name']).last()
            if tank:
                tank.tank_quantity += float(request.data['actual_quantity'])
                tank.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    except Exception as error:
        return Response({"message" : f"an error occurred : {error}"}, status=status.HTTP_400_BAD_REQUEST)