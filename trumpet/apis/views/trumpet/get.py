from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from ...serializers import TrumpetSerializer
from ....models import Trumpet
from rest_framework import status

@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_trumpets(request):
    try:
        trumpets= Trumpet.objects.all()
        serializer= TrumpetSerializer(trumpets, many= True)
        return Response(serializer.data, status= status.HTTP_200_OK)
    except Trumpet.DoesNotExist:
        return Response('Sorry your request not found :(')
    except Exception as error:
        return Response({"message" : f"an error accrued : {error}"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET",])    
@permission_classes([IsAdminUser])
def get_trumpets_by_material(request, material_name):
    try:
        trumpets = Trumpet.objects.filter(subject_name=material_name)
        serializer = TrumpetSerializer(trumpets, many=True).data
        return Response({
            "data": serializer
        }, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response({
            "message": "an error occurred while getting trumpets"
        }, status=status.HTTP_400_BAD_REQUEST)