from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from ...models import ShiftDetails, BranchesInformation, BasicInformationAboutTheStation

@api_view(['DELETE'])
@permission_classes({IsAdminUser})
def delete_basic_information_about_the_station(request, pk):
    try:
        query= BasicInformationAboutTheStation.objects.get(id= pk)
        query.delete()
        return Response('DELETED :)', status= HTTP_200_OK)
    except Exception as error:
        return Response(f'sorry there are error while deleting this model: {error}', status= HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
@permission_classes({IsAdminUser})
def delete_branches_information(request, pk):
    try:
        query= BranchesInformation.objects.get(id= pk)
        query.delete()
        return Response('DELETED :)', status= HTTP_200_OK)
    except Exception as error:
        return Response(f'sorry there are error while deleting this model: {error}', status= HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
@permission_classes({IsAdminUser})
def delete_shift_details(request, pk):
    try:
        query= ShiftDetails.objects.get(id= pk)
        query.delete()
        return Response('DELETED :)', status= HTTP_200_OK)
    except Exception as error:
        return Response(f'sorry there are error while deleting this model: {error}', status= HTTP_400_BAD_REQUEST)