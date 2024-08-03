from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from ....models import Cars, Subjects, NewCustomer
from ...serializers import CarsSerializer, SubjectsSerializer, NewCustomerSerializer

@api_view(['PUT'])
@permission_classes([IsAdminUser])
def update_new_customer(request, pk):
    try:
        customer= NewCustomer.objects.get(sequence= pk)
        car= Cars.objects.get(customer= customer)
        subject= Subjects.objects.get(customer= customer)

        customer_data = request.data.get('customer')
        customer_serializer= NewCustomerSerializer(customer, data= customer_data)
        if customer_serializer.is_valid():
            customer_serializer.save()
        else:
            return Response({'message': 'Please correct your customer data :(', 'errors': customer_serializer.errors}, status= HTTP_400_BAD_REQUEST)
        car_data = request.data.get('cars')
        car_serializer= CarsSerializer(car, data = car_data)
        if car_serializer.is_valid():
            car_serializer.save()
        else:
            return Response({'message': 'Please correct your car data :(', 'errors': car_serializer.errors}, status= HTTP_400_BAD_REQUEST)
        subject_data = request.data.get('subjects')
        subject_serializer= SubjectsSerializer(subject, data = subject_data)
        if subject_serializer.is_valid():
            subject_serializer.save()
        else:
            return Response({'message': 'Please correct your subject data :(', 'errors': subject_serializer.errors}, status= HTTP_400_BAD_REQUEST)
        data= {
            'customer': customer_serializer.data,
            'car': car_serializer.data,
            'subject': subject_serializer.data
        }
        return Response(data, status= HTTP_400_BAD_REQUEST)
    except Exception as error:
        return Response({'message' : f'an error occurred : {error}'}, status= HTTP_400_BAD_REQUEST)