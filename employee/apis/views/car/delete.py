from rest_framework import decorators, status
from rest_framework.response import Response
from employee.models import Car


@decorators.api_view(['DELETE'])
def delete_car (request, carcode) : 
    try : 
        
        try : 
            car = Car.objects.get(car_code=carcode)
        except Car.DoesNotExist :
            return Response({
                'message' : f'car does not exist'
            },status=status.HTTP_404_NOT_FOUND)
            
        car.delete()

        return Response({
            'message' : 'car deleted successfully'
        },status=status.HTTP_200_OK)

    except Exception as error :
        return Response({
            'message' : f'an error accured : {error}'
        },status=status.HTTP_400_BAD_REQUEST)