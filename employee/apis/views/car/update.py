from rest_framework import decorators, status
from rest_framework.response import Response
from employee.apis.serializers import CarSerializer
from employee.models import Car


@decorators.api_view(['PUT'])
def update_car (request, carcode) : 
    try : 
        
        try : 
            emp = Car.objects.get(car_code=carcode)
        except Car.DoesNotExist : 
            return Response({
                'message' : "car with this id doesn't found"
            },status=status.HTTP_404_NOT_FOUND)

        serializer = CarSerializer(emp,request.data)

        if serializer.is_valid() : 
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    except Exception as error :
        return Response({
            'message' : f'an error accured : {error}'
        },status=status.HTTP_400_BAD_REQUEST)