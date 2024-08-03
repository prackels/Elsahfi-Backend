from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from ...serializers import ShiftCashSerializer
from ....models import ShiftCash
from rest_framework import status
from django.db.models import Sum

@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_shift_cash(request):
    try:
        query = ShiftCash.objects.all()
        serializer = ShiftCashSerializer(query, many=True)
        total_shift_cash = ShiftCash.objects.aggregate(total= Sum('shift_cash'))['total']
        total = ShiftCash.objects.aggregate(total= Sum('total_amount'))['total']
        net = ShiftCash.objects.aggregate(total= Sum('net_total'))['total']
        data = {
            "Cash": total_shift_cash,
            "Total": total,
            "Net": net,
            "Data": serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)
    except ShiftCash.DoesNotExist:
        return Response('Sorry your request not found :(', status=status.HTTP_404_NOT_FOUND)
    except Exception as error:
        return Response({"message": f"an error occurred: {error}"}, status=status.HTTP_400_BAD_REQUEST)
