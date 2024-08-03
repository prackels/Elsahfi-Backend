from rest_framework import status, decorators, permissions
from rest_framework.response import Response
from shift.models import BranchesInformation
from shift.apis.serializers import ShiftSerializer
from globals.real_time_activity import SendRealTimeActivity
from shift.tasks import close_shift_automatically

@decorators.api_view(['POST'])
@decorators.permission_classes([permissions.IsAdminUser])
def CreateShift (request) : 
    data = request.data.copy()

    try:
        branch = BranchesInformation.objects.get(branch_number=data.get("branch_number"))
    except BranchesInformation.DoesNotExist:
        return Response({
            "message": "Branch doesn't exists with this number"
        }, status=status.HTTP_404_NOT_FOUND)
    try : 
        data = request.data.copy()
        data['user'] = request.user.id
        data["branch_number"] = branch.pk
        serialzier = ShiftSerializer(data=data)
        if serialzier.is_valid() : 
            serialzier.save()
            SendRealTimeActivity(
                content="New Shift Started",
                from_user=request.user
            )
            # close_shift_automatically.delay()
            return Response(serialzier.get_uid(),status=status.HTTP_200_OK)
        return Response(serialzier.errors,status=status.HTTP_400_BAD_REQUEST)
        
    except Exception as error :
        return Response({
            'message' : f'an error accured : {error}'
        },status=status.HTTP_400_BAD_REQUEST)