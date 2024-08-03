from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.permissions import IsAdminUser
from django.shortcuts import get_object_or_404
from ....models import NewCustomer
from globals.real_time_activity import SendRealTimeActivity as SendNotification

@api_view(['POST'])
@permission_classes([IsAdminUser])
def block_customer(request, pk):
    customer = get_object_or_404(NewCustomer, pk=pk)
    if customer.blocked == True:
        return Response('already blocked')
    else:
        customer.blocked = True
        customer.save()
        content = f'the customer has been blocked "{customer.customer_name}"'
        SendNotification(
            noti_type = "block",
            content = content,
            from_user=request.user
        )
        return Response({'message': 'Customer has been blocked successfully.'}, status=HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def unblock_customer(request, pk):
    customer = get_object_or_404(NewCustomer, pk=pk)
    if customer.blocked== False:
        return Response('already unblocked')
    else:
        customer.blocked = False
        customer.save()
        content = f'the customer has been unblocked "{customer.customer_name}"'
        SendNotification(
            noti_type = "unblock",
            content = content,
            from_user=request.user
        )
        return Response({'message': 'Customer has been unblocked successfully.'}, status=HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def pend_customer(request, pk):
    customer = get_object_or_404(NewCustomer, pk=pk)
    if customer.pending== True:
        return Response('already pend')
    else:
        customer.pending = True
        customer.save()
        return Response({'message': 'Customer has been marked as pending successfully.'}, status=HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def unpend_customer(request, pk):
    customer = get_object_or_404(NewCustomer, pk=pk)
    if customer.pending== False:
        return Response('already unpend')
    else:
        customer.pending = False
        customer.save()
        return Response({'message': 'Customer is no longer pending.'}, status=HTTP_200_OK)
