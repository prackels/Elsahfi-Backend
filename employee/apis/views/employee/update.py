from rest_framework import decorators, status, permissions
from rest_framework.response import Response
from employee.apis.serializers import EmployeeSerializer
from employee.models import Employee
from globals.real_time_activity import SendRealTimeActivity


@decorators.api_view(['PUT'])
@decorators.permission_classes([permissions.IsAdminUser])
def update_employee (request, employeeid) : 
    try : 
        
        try : 
            emp = Employee.objects.get(id=employeeid)
        except Employee.DoesNotExist : 
            return Response({
                'message' : "emplyee with this id doesn't found"
            },status=status.HTTP_404_NOT_FOUND)

        serializer = EmployeeSerializer(emp,data=request.data)

        if serializer.is_valid() : 
            serializer.save()
            SendRealTimeActivity(
                content="update employee",
                from_user=request.user
            )
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    except Exception as error :
        return Response({
            'message' : f'an error accured : {error}'
        },status=status.HTTP_400_BAD_REQUEST)