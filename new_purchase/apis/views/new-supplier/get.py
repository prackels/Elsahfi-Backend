from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from ...serializers import NewSupplierSerializer
from ....models import NewSupplier
from rest_framework import status

@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_new_supplier(request):
    try:
        query= NewSupplier.objects.all()
        serializer= NewSupplierSerializer(query, many= True)
        all_suppliers= query.count()
        data= {
            'suppliers': all_suppliers,
            'data': serializer.data
        }
        return Response(data, status= status.HTTP_200_OK)
    except NewSupplier.DoesNotExist:
        return Response('Sorry your request not found :(')
    except Exception as error:
        return Response({"message" : f"an error accured : {error}"}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET",])
@permission_classes([IsAdminUser])
def get_new_supplier_byname(request, supplier_name):
    try:
        query= NewSupplier.objects.filter(supplier_name__icontains=supplier_name)
        serializer= NewSupplierSerializer(query, many= True)
        return Response({
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            "message": f"an error occurred {e}"
        }, status=status.HTTP_400_BAD_REQUEST)