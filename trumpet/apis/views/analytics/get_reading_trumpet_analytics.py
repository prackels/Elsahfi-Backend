from rest_framework import decorators,permissions, status
from rest_framework.response import Response
from rest_framework.decorators import permission_classes, api_view
from ...serializers import AnalyticsSerializer
from ....models import ReadingTrumpet
from datetime import datetime, timedelta
from django.db.models import Sum

@api_view(["GET"])
@permission_classes([permissions.IsAdminUser])
def get_reading_trumpet_with_date(request, from_date, to_date):
    try:
        reading_in_this_week = ReadingTrumpet.objects.filter(date__range=(from_date, to_date))\
            .values('trumpet_number')\
            .annotate(total_sold=Sum('quantity_sold'), total_price=Sum('total'))
        return Response(reading_in_this_week, status=status.HTTP_200_OK)
    except Exception as error:
        return Response({'message': f'an error occurred: {error}'}, status=status.HTTP_400_BAD_REQUEST)