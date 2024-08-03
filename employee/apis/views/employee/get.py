from rest_framework import decorators, status
from rest_framework.response import Response
from employee.apis.serializers import EmployeeSerializer
from employee.models import Employee


@decorators.api_view(['GET'])
def get_employee (request) : 
    try : 
        queyrset = Employee.objects.all()
        serializer = EmployeeSerializer(queyrset, many=True)
        employees_total= queyrset.count()
        data= {
            'Employees': employees_total,
            'data': serializer.data

        }
        return Response(data,status=status.HTTP_200_OK)
    except Exception as error :
        return Response({
            'message' : f'an error accured : {error}'
        },status=status.HTTP_400_BAD_REQUEST)
    
@decorators.api_view(["GET",])
def get_employee_byname(request, employee_name):
    try:
        employees = Employee.objects.filter(name=employee_name)
        serializer = EmployeeSerializer(employees, many=True)
        return Response({
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            "message": f"an error occurred {e}"
        }, status=status.HTTP_404_NOT_FOUND)