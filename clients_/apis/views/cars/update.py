from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from ....models import Cars
from ...serializers import CarsSerializer

@api_view(['PUT'])
@permission_classes([IsAdminUser])
def update_client_car(request, pk):
    try:
        try:
            car= Cars.objects.get(id= pk)
        except Cars.DoesNotExist:
            return Response('sorry this model not found :(', status= HTTP_400_BAD_REQUEST)
        serializer = CarsSerializer(car, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=HTTP_200_OK)
        else:
            return Response(serializer.errors, status= HTTP_400_BAD_REQUEST)
    except Exception as error:
        return Response({"message" : f"an error occurred : {error}"}, status= HTTP_400_BAD_REQUEST)