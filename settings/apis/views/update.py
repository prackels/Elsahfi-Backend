from rest_framework import decorators, status, permissions
from rest_framework.response import Response
from ...models import BranchesInformation, ShiftDetails, BasicInformationAboutTheStation
from ..serializers import BranchesInformationSerializer, ShiftDetailsSerializer, BasicInformationAboutTheStationSerializers

@decorators.api_view(['PUT'])
@decorators.permission_classes([permissions.IsAdminUser])
def update_basic_information_about_the_station(request, pk): 
    try:
        try:
            query = BasicInformationAboutTheStation.objects.get(id=pk)
        except BasicInformationAboutTheStation.DoesNotExist:
            return Response('sorry this model not found :()', status=status.HTTP_404_NOT_FOUND)
        serializer = BasicInformationAboutTheStationSerializers(query, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as error:
        return Response({"message" : f"an error accured : {error}"}, status=status.HTTP_400_BAD_REQUEST)
    
@decorators.api_view(['PUT'])
@decorators.permission_classes([permissions.IsAdminUser])
def update_branches_information(request, pk): 
    try:
        try:
            query = BranchesInformation.objects.get(id=pk)
        except BranchesInformation.DoesNotExist:
            return Response('sorry this model not found :()', status=status.HTTP_404_NOT_FOUND)
        serializer = BranchesInformationSerializer(query, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as error:
        return Response({"message" : f"an error accured : {error}"}, status=status.HTTP_400_BAD_REQUEST)

@decorators.api_view(['PUT'])
@decorators.permission_classes([permissions.IsAdminUser])
def update_shift_details(request, pk): 
    try:
        try:
            query = ShiftDetails.objects.get(id=pk)
        except ShiftDetails.DoesNotExist:
            return Response('sorry this model not found :()', status=status.HTTP_404_NOT_FOUND)
        serializer = ShiftDetailsSerializer(query, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as error:
        return Response({"message" : f"an error accured : {error}"}, status=status.HTTP_400_BAD_REQUEST)