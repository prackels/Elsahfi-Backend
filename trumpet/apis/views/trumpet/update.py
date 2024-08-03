from rest_framework import decorators, status, permissions
from rest_framework.response import Response
from ....models import Trumpet
from ...serializers import TrumpetSerializer

@decorators.api_view(['PUT'])
@decorators.permission_classes([permissions.IsAdminUser])
def update_trumpet(request, pk): 
    try:
        try:
            query = Trumpet.objects.get(sequence=pk)
        except Trumpet.DoesNotExist:
            return Response('sorry this model not found :(', status=status.HTTP_404_NOT_FOUND)
        serializer = TrumpetSerializer(query, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as error:
        return Response({"message" : f"an error accrued : {error}"}, status=status.HTTP_400_BAD_REQUEST)
