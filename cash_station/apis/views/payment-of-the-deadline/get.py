from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from ...serializers import PaymentOfTheDeadlineSerializer, CashSerializer
from ....models import PaymentOfTheDeadLine, Cash
from rest_framework import status
from django.db.models import Sum
@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_payment_of_the_dead_line(request):
    try:
        query= PaymentOfTheDeadLine.objects.all()
        serializer= PaymentOfTheDeadlineSerializer(query, many= True)
        financial_advance= PaymentOfTheDeadLine.objects.aggregate(total= Sum('cash__financial_advance'))['total']
        the_amount_required= PaymentOfTheDeadLine.objects.aggregate(total= Sum('cash__the_amount_required'))['total']
        remaining_for_the_station= PaymentOfTheDeadLine.objects.aggregate(total= Sum('remaining_for_the_station'))['total']
        data= {
            'total_amount_required': the_amount_required,
            'total_paid': financial_advance,
            'remaining_for_the_station': remaining_for_the_station,
            'data': serializer.data
        }
        return Response(data, status= status.HTTP_200_OK)
    except PaymentOfTheDeadLine.DoesNotExist:
        return Response('Sorry your request not found :(')
    except Exception as error:
        return Response({"message" : f"an error occurred : {error}"}, status=status.HTTP_400_BAD_REQUEST)





@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_cash_with_customer_name(request):
    try:
        query= Cash.objects.get(customer= request.data.get('customer_name'))
        serializer= CashSerializer(query, many= True)
        return Response(serializer.data, status= status.HTTP_200_OK)
    except Cash.DoesNotExist:
        return Response('an error occurred :(')
    except Exception as error:
        return Response({"message" : f"an error occurred : {error}"}, status=status.HTTP_400_BAD_REQUEST)
