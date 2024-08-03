from rest_framework import decorators,permissions, status
from rest_framework.response import Response
from clients_.apis.serializers import NewCustomerSerializer, SubjectsSerializer, CarsSerializer
from clients_.models import NewCustomer, Cars, Subjects
from employee.models import Car
from employee.apis.serializers import CarSerializer
from codes.models import Code
from codes.apis.serializers import CodeSerializer
from trumpet.models import Trumpet
from trumpet.apis.serializers import TrumpetSerializer
from settings.models import BranchesInformation
from settings.apis.serializers import BranchesInformationSerializer

###################################################################################################################################################
### Get Customer Info With Out a Subjects and Cars ###
@decorators.api_view(['POST'])
@decorators.permission_classes([permissions.IsAdminUser])
def get_customer_info(request, customer):
    try:
        query= NewCustomer.objects.filter(customer_name__icontains= customer)
        if NewCustomer.DoesNotExist:
            return Response('Customer Info not found :(', status=status.HTTP_400_BAD_REQUEST)
        serializer= NewCustomerSerializer(query, many= True)
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)
    except Exception as error:
        return Response({"message": f"an error occurred: {error}"}, status=status.HTTP_400_BAD_REQUEST)
###################################################################################################################################################
### Get Customer Info With Out a Subjects and Cars ###
@decorators.api_view(['POST'])
@decorators.permission_classes([permissions.IsAdminUser])
def get_customer_info_with_cars_subjects(request, customer):
    try:
        query = NewCustomer.objects.filter(customer_name__icontains=customer)
        
        if query.exists():
            customer_serializer = NewCustomerSerializer(query, many=True)
            cars = Cars.objects.filter(customer=query.first())
            cars_serializer = CarsSerializer(cars, many=True)
            subjects = Subjects.objects.filter(customer=query.first())
            subjects_serializer = SubjectsSerializer(subjects, many=True)
            data = {
                'customer': customer_serializer.data,
                'cars': cars_serializer.data,
                'subjects': subjects_serializer.data
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response('Customer Info not found :(', status=status.HTTP_400_BAD_REQUEST)
    except Exception as error:
        return Response({"message": f"An error occurred: {error}"}, status=status.HTTP_400_BAD_REQUEST)
###################################################################################################################################################
### Get Full Info About Car ###
@decorators.api_view(['POST'])
@decorators.permission_classes([permissions.IsAdminUser])
def station_cars(request, car):
    try:
        query= Car.objects.filter(car_name__icontains= car)
        if Car.DoesNotExist:
            return Response('Car Info not found :(', status=status.HTTP_400_BAD_REQUEST)
        serializer= CarSerializer(query, many= True)
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)
    except Exception as error:
        return Response({"message": f"an error occurred: {error}"}, status=status.HTTP_400_BAD_REQUEST)
###################################################################################################################################################
    ### Get Full Info About Codes ###
@decorators.api_view(['POST'])
@decorators.permission_classes([permissions.IsAdminUser])
def codes(request, code):
    try:
        query= Code.objects.filter(code__icontains= code)
        if Code.DoesNotExist:
            return Response('Code Info not found :(', status=status.HTTP_400_BAD_REQUEST)
        serializer= CodeSerializer(query, many= True)
        return Response(serializer.data, status= status.HTTP_200_OK)
    except Exception as error:
        return Response({"message": f"an error occurred: {error}"}, status=status.HTTP_400_BAD_REQUEST)
###################################################################################################################################################
    ### Get Trumpet
@decorators.api_view(['POST'])
@decorators.permission_classes([permissions.IsAdminUser])
def codes(request, id):
    try:
        query= Code.objects.filter(code__icontains= code)
        if Code.DoesNotExist:
            return Response('Code Info not found :(', status=status.HTTP_400_BAD_REQUEST)
        serializer= CodeSerializer(query, many= True)
        return Response(serializer.data, status= status.HTTP_200_OK)
    except Exception as error:
        return Response({"message": f"an error occurred: {error}"}, status=status.HTTP_400_BAD_REQUEST)
###################################################################################################################################################
    ### Get Trumpet K
@decorators.api_view(['GET'])
@decorators.permission_classes([permissions.IsAdminUser])
def get_trumpet_k(request):
    try:
        query= Trumpet.objects.filter(name= "الطرومبه k")
        if not query.exists():
            return Response('Trumpet K Info not found :(', status=status.HTTP_400_BAD_REQUEST)
        serializer= TrumpetSerializer(query, many= True)
        return Response(serializer.data, status= status.HTTP_200_OK)
    except Exception as error:
        return Response({"message": f"an error occurred: {error}"}, status=status.HTTP_400_BAD_REQUEST)
###################################################################################################################################################
    ### Get Branches
@decorators.api_view(['GET'])
@decorators.permission_classes([permissions.IsAdminUser])
def get_branches(request, id):
    try:
        query= BranchesInformation.objects.filter(id__icontains= id)
        if not query.exists():
            return Response('Branch Info not found :(', status=status.HTTP_400_BAD_REQUEST)
        serializer= BranchesInformationSerializer(query, many= True)
        return Response(serializer.data, status= status.HTTP_200_OK)
    except Exception as error:
        return Response({"message": f"an error occurred: {error}"}, status=status.HTTP_400_BAD_REQUEST)