from rest_framework import decorators, permissions, status
from rest_framework.response import Response
from ..serializers import BranchesInformationSerializer, ShiftDetailsSerializer, BasicInformationAboutTheStationSerializers
from ...models import BranchesInformation, ShiftDetails, BasicInformationAboutTheStation

@decorators.api_view(['GET'])
@decorators.permission_classes([permissions.IsAdminUser])
def get_basic_information_about_the_station(request):
    try:
        query= BasicInformationAboutTheStation.objects.all()
        serializer= BasicInformationAboutTheStationSerializers(query, many= True)
        return Response(serializer.data, status= status.HTTP_200_OK)
    except Exception as error:
        return Response({"message" : f"an error accured : {error}"}, status=status.HTTP_400_BAD_REQUEST)

@decorators.api_view(['GET'])
@decorators.permission_classes([permissions.IsAdminUser])
def get_branches_information(request):
    try:
        query= BranchesInformation.objects.all()
        serializer= BranchesInformationSerializer(query, many= True)
        data= {'branches': serializer.data,
        }
        return Response(data, status= status.HTTP_200_OK)
    except Exception as error:
        return Response({"message" : f"an error accured : {error}"}, status=status.HTTP_400_BAD_REQUEST)

@decorators.api_view(['GET'])
@decorators.permission_classes([permissions.IsAdminUser])
def get_shift_details(request):
    try:
        query= ShiftDetails.objects.all()
        total_shifts= ShiftDetails.objects.aaggregate()
        serializer= ShiftDetailsSerializer(query, many= True)
        data= {'all shifts': serializer.data,
               'total_shifts':total_shifts,
        }
        return Response(data, status= status.HTTP_200_OK)
    except Exception as error:
        return Response({"message" : f"an error accured : {error}"}, status=status.HTTP_400_BAD_REQUEST)