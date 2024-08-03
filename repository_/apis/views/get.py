from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from ..serializers import RepositorySerializer
from ...models import Repository
from rest_framework import status
from django.db.models import Sum

@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_repositories(request):
    try:
        total_quantities = Repository.objects.aggregate(total_quantity=Sum('quantity'))['total_quantity']
        total_totals = Repository.objects.aggregate(total_total=Sum('total'))['total_total']
        get_repositories = Repository.objects.annotate(
            total_quantity=Sum('quantity'),
            total_total=(Sum('total') * Sum('quantity'))
        )
        serializer = RepositorySerializer(get_repositories, many=True)
        response_data = {
            'total_quantity': total_quantities or 0,
            'total_total': total_totals or 0,
            'repositories': serializer.data
        }
        return Response(response_data, status= status.HTTP_200_OK)
    except Repository.DoesNotExist:
        return Response('Sorry your request not found :(')
    except Exception as error:
        return Response({"message" : f"an error occurred : {error}"}, status=status.HTTP_400_BAD_REQUEST)
    
