from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.permissions import IsAdminUser
from ....models import PaymentOfTheDeadLine
from django.core.exceptions import ObjectDoesNotExist

@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def delete_payment_of_the_dead_line(request, pk):
    try:    
        try:
            query= PaymentOfTheDeadLine.objects.get(sequence= pk)
            query.delete()
            return Response('DELETED :)', status= HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response('ur request not found :(', status=HTTP_400_BAD_REQUEST)
    except Exception as error:
        return Response(f'sorry there are error :( {error}', status= HTTP_400_BAD_REQUEST)