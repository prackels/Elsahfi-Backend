from rest_framework import decorators,permissions, status
from rest_framework.response import Response
from expenses.apis.serializers import GovernmentExpSerializer
from globals.real_time_activity import SendRealTimeActivity
from codes.models import Code

@decorators.api_view(['POST'])
@decorators.permission_classes([permissions.IsAdminUser])
def create_gov_expenses (request) : 
    data = request.data.copy()

    try:
        code = Code.objects.get(code=data.get("expense_code"))
    except Code.DoesNotExist:
        return Response({
            "message": "Code doesn't exists"
        }, status=status.HTTP_404_NOT_FOUND)
    try : 
        data["expense_code"] = code.pk
        serializer = GovernmentExpSerializer(data=data)
        if serializer.is_valid() : 
            serializer.save()
            SendRealTimeActivity(
                content="create government expense",
                from_user=request.user
            )
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    except Exception as error :
        return Response({
            'message' : f'an error accured : {error}'
        },status=status.HTTP_400_BAD_REQUEST)