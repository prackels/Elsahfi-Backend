from rest_framework import decorators, status, permissions
from rest_framework.response import Response
from ....models import PaymentOfTheDeadLine, Cash
from ...serializers import PaymentOfTheDeadlineSerializer, CashSerializer

@decorators.api_view(['PUT'])
@decorators.permission_classes([permissions.IsAdminUser])
def update_payment_of_the_dead_line(request, pk): 
    try:
        try:
            query = PaymentOfTheDeadLine.objects.get(sequence=pk)
        except PaymentOfTheDeadLine.DoesNotExist:
            return Response('sorry this model not found :(', status=status.HTTP_404_NOT_FOUND)
        serializer = PaymentOfTheDeadlineSerializer(query, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as error:
        return Response({"message" : f"an error occurred : {error}"}, status=status.HTTP_400_BAD_REQUEST)
    


@decorators.api_view(['PUT'])
@decorators.permission_classes([permissions.IsAdminUser])
def update_cash(request, pk): 
    try:
        try:
            query = Cash.objects.get(id=pk)
        except Cash.DoesNotExist:
            return Response('sorry this model not found :(', status=status.HTTP_404_NOT_FOUND)
        serializer = CashSerializer(query, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as error:
        return Response({"message" : f"an error occurred : {error}"}, status=status.HTTP_400_BAD_REQUEST)