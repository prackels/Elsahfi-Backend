from rest_framework import decorators, status, permissions
from ...serializers import TrumpetSerializer
from ....models import Trumpet
from rest_framework.response import Response

@decorators.api_view(['POST'])
@decorators.permission_classes([permissions.IsAdminUser])
def create_trumpet(request):
    try:
        trumpet= request.data.get('name')
        existing_trumpet = Trumpet.objects.filter(name= trumpet)
        if existing_trumpet:
            return Response({'error': 'Trumpet with the same name already exists'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = TrumpetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except Exception as error:
        return Response({"message" : f"an error occurred : {error}"}, status=status.HTTP_400_BAD_REQUEST)