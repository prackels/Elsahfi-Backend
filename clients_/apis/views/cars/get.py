from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from ....models import Cars, NewCustomer
from ...serializers import CarsSerializer, CustomersCarsSerializer

@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_cars(request):
    try:
        cars_data = []
        customers = NewCustomer.objects.all()
        for customer in customers:
            cars = Cars.objects.filter(customer=customer)
            cars_serializer = CarsSerializer(cars, many=True)
            cars_data.append({
                'customer': customer.customer_name,
                'cars': cars_serializer.data
            })
        total_cars = Cars.objects.all().count()
        response_data = {
            'cars_data': cars_data,
            'total_cars': total_cars
        }
        return Response(response_data, status=HTTP_200_OK)
    except Exception as error:
        return Response(f"Sorry, there was a problem while getting the data: {error}", status=HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_all_cars(request):
    try:
        cars = Cars.objects.all()
        total_cars = Cars.objects.all().count()
        serializer = CustomersCarsSerializer(cars, many=True)
        return Response({
            "data": serializer.data,
            "total_cars": total_cars
        }, status=HTTP_200_OK)
    except Exception as e:
        return Response({
            "message": "an error occurred while getting all cars"
        }, status=HTTP_400_BAD_REQUEST)
    

@api_view(["GET"])
def get_customer_cars(request, customer_name):
    try:
        query = Cars.objects.filter(customer__customer_name=customer_name)
        serializer = CarsSerializer(query, many=True).data
        return Response({
            "data": serializer
        }, status=HTTP_200_OK)
    except Exception as error:
        return Response(f"Sorry, there was a problem while getting the data: {error}", status=HTTP_400_BAD_REQUEST)