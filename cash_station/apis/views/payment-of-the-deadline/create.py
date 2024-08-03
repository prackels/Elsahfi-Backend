from rest_framework import decorators,permissions, status
from rest_framework.response import Response
from ...serializers import PaymentOfTheDeadlineSerializer
from clients_.models import NewCustomer

@decorators.api_view(['POST'])
@decorators.permission_classes([permissions.IsAdminUser])
def create_payment_of_the_dead_line(request):
    data = request.data.copy()

    try:
        customer = NewCustomer.objects.get(customer_name=data.get("customer_name"))
    except NewCustomer.DoesNotExist:
        return Response({
            "message": "Supplier doesn't exists"
        }, status=status.HTTP_404_NOT_FOUND)
    try : 
        data["customer_name"] = customer.pk
        serializer = PaymentOfTheDeadlineSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except Exception as error:
        return Response({"message" : f"an error accured : {error}"}, status=status.HTTP_400_BAD_REQUEST)