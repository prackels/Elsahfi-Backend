from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from ...serializers import NewSupplierSerializer
from rest_framework. status import HTTP_400_BAD_REQUEST, HTTP_200_OK

@api_view(['POST'])
@permission_classes([IsAdminUser])
def create_new_supplier(request):
        try:
            supplier_serializer = NewSupplierSerializer(data=request.data)
            if supplier_serializer.is_valid():
                supplier_serializer.save()
                return Response(supplier_serializer.data, status= HTTP_200_OK)
            else:
                print(supplier_serializer.errors)
                return Response('please correct the data :(', status=HTTP_400_BAD_REQUEST)
        except Exception as error:
            return Response(f'There is an error: {error}', status= HTTP_400_BAD_REQUEST)