from rest_framework import decorators, status
from rest_framework.response import Response
from employee.apis.serializers import CarSerializer
from employee.models import Car
from clients_.models import Cars
from clients_.apis.serializers import CarsSerializer


@decorators.api_view(['GET'])
def get_cars (request) : 
    try : 
        queyrset = Car.objects.all()
        serializer = CarSerializer(queyrset, many=True)
        cars_total= queyrset.count()
        data= {
            'Cars': cars_total,
            'data': serializer.data,
        }
        return Response(data,status=status.HTTP_200_OK)
    except Exception as error :
        return Response({
            'message' : f'an error accured : {error}'
        },status=status.HTTP_400_BAD_REQUEST)
    
@decorators.api_view(["GET"])
def get_cars_bytype(request, car_type):
    try : 
        queyrset = Car.objects.filter(type_of_car__icontains=car_type)
        serializer = CarSerializer(queyrset, many=True)
        cars_total= queyrset.count()
        data= {
            'cars': cars_total,
            'data': serializer.data,
        }
        return Response(data,status=status.HTTP_200_OK)
    except Exception as error :
        return Response({
            'message' : f'an error occurred : {error}'
        },status=status.HTTP_400_BAD_REQUEST)
