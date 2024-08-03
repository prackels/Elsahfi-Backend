from rest_framework import decorators, status, permissions
from rest_framework.response import Response
from employee.models import Employee
from globals.real_time_activity import SendRealTimeActivity


@decorators.api_view(['DELETE'])
@decorators.permission_classes([permissions.IsAdminUser])
def delete_employee (request, employeeid) : 
    try : 
        
        try : 
            emplyee = Employee.objects.get(id=employeeid)
        except Employee.DoesNotExist :
            return Response({
                'message' : f'emplyee does not exist'
            },status=status.HTTP_404_NOT_FOUND)
            
        emplyee.delete()

        SendRealTimeActivity(
            content="delete employee",
            from_user=request.user
        )

        return Response({
            'message' : 'employee deleted successfully'
        },status=status.HTTP_200_OK)

    except Exception as error :
        return Response({
            'message' : f'an error accured : {error}'
        },status=status.HTTP_400_BAD_REQUEST)