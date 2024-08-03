from rest_framework import decorators, status, permissions
from rest_framework.response import Response
from employee.apis.serializers import CarSerializer
from employee.models import Car

@decorators.api_view(['POST'])
@decorators.permission_classes([permissions.IsAdminUser])
def create_car(request):
    try:
        serializer = CarSerializer(data=request.data)
        car_exists = Car.objects.filter(car_name=request.data['car_name']).exists()
        
        if not car_exists:
            serializer = CarSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Car with the same name already exists'}, status=status.HTTP_400_BAD_REQUEST)
            
    except Exception as error:
        return Response({'message': f'an error occurred: {error}'}, status=status.HTTP_400_BAD_REQUEST)
