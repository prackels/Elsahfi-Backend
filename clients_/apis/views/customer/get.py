from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from ....models import NewCustomer
from ...serializers import NewCustomerSerializer

@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_new_customer(request):
    try:
        customers = NewCustomer.objects.all()
        customer_serializer = NewCustomerSerializer(customers, many=True)
        total_clients= NewCustomer.objects.all().count()
        customer_data = {
            'customer': customer_serializer.data,
            'customers_total': total_clients,
            }
        return Response(customer_data, status=HTTP_200_OK)
    except Exception as error:
        return Response(f"Sorry, there was a problem while getting the data: {error}", status=HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_new_customer_byname(request, customer_name):
    try:
        customers = NewCustomer.objects.filter(blocked=False).filter(pending=False).filter(customer_name__icontains=customer_name)
        customer_serializer = NewCustomerSerializer(customers, many=True)
        customer_data = {
            'customer': customer_serializer.data,
            }
        return Response(customer_data, status=HTTP_200_OK)
    except Exception as error:
        return Response(f"Sorry, there was a problem while getting the data: {error}", status=HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_pending_customers(request):
    try:
        customers = NewCustomer.objects.filter(pending=True)
        customer_serializer = NewCustomerSerializer(customers, many=True)
        total_clients= customers.count()
        customer_data = {
            'customer': customer_serializer.data,
            'customers_total': total_clients,
            }
        return Response(customer_data, status=HTTP_200_OK)
    except Exception as error:
        return Response(f"Sorry, there was a problem while getting the data: {error}", status=HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_blocked_customers(request):
    try:
        customers = NewCustomer.objects.filter(blocked=True)
        customer_serializer = NewCustomerSerializer(customers, many=True)
        total_clients= customers.count()
        customer_data = {
            'customer': customer_serializer.data,
            'customers_total': total_clients,
            }
        return Response(customer_data, status=HTTP_200_OK)
    except Exception as error:
        return Response(f"Sorry, there was a problem while getting the data: {error}", status=HTTP_400_BAD_REQUEST)