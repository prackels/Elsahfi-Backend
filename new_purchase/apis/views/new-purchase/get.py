from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from shift.models import Shift
from ...serializers import NewPurchaseSerializer
from ....models import NewPurchase
from rest_framework import status

@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_new_purchase(request):
    try:
        query= NewPurchase.objects.all()
        serializer= NewPurchaseSerializer(query, many= True)
        # gasoline_91_quantity = NewPurchase.objects.filter(subject_name='Premium Gasoline 91').aggregate(total_quantity=Sum(''))['total_quantity']
        # gasoline_95_quantity = NewPurchase.objects.filter(subject_name='Premium Gasoline 95').aggregate(total_quantity=Sum(''))['total_quantity']
        # diesel_quantity = NewPurchase.objects.filter(subject_name='Diesel').aggregate(total_quantity=Sum(''))['total_quantity']
        # total_quantity = NewPurchase.objects.aggregate(total_quantity=Sum(''))['total_quantity']

        # response_data= {'total_91': gasoline_91_quantity,
        #                 'total_95': gasoline_95_quantity,
        #                 'total_diesel': diesel_quantity,
        #                 'total_sold': total_quantity,
        #                 'data': serializer.data,
        #                 }


        return Response(serializer.data, status= status.HTTP_200_OK)
    except NewPurchase.DoesNotExist:
        return Response('Sorry your request not found :(')
    except Exception as error:
        return Response({"message" : f"an error occurred : {error}"}, status=status.HTTP_400_BAD_REQUEST)
    



@api_view(["GET"])
@permission_classes([IsAdminUser])
def get_purchase_count(request):
    try:
        shift_instance= Shift.objects.filter(is_active= False).last()
        if shift_instance:
            query= NewPurchase.objects.filter(shift= shift_instance).count()
            return Response(query,status=status.HTTP_200_OK)
        else:
            return Response('sorry no shift data :(', status= status.HTTP_400_BAD_REQUEST)
    except Exception as error:
        return Response(f'An error occurred while processing your request {error}', status=status.HTTP_400_BAD_REQUEST)