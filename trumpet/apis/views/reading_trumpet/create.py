from rest_framework.decorators import permission_classes, api_view
from rest_framework import status, permissions
from rest_framework.response import Response

from tank.models import Tank
from ...serializers import ReadingTrumpetKSerializer
from ....models import ReadingTrumpet, Trumpet

@api_view(['POST'])
@permission_classes([permissions.IsAdminUser])
def create_reading_trumpet(request):
    data = request.data

    if not data:
        return Response({
            "message": "please insert data"
        }, status=status.HTTP_400_BAD_REQUEST)
    
    subject_name= data.get("subject_name")
    trumpet_number = data.get("trumpet_number")
    trumpet_caliber= data.get("trumpet_caliber") 
    receiving_counter= data.get("receiving_counter")
    delivery_counter= data.get("delivery_counter") # عداد التسليم
    quantity_sold= data.get("quantity_sold") # الكميه  المباعه باللتر
    price_per_litre= data.get("price_per_litre") # السعر باللتر
    total= data.get("total") # اجمالي باللتر
    comments= data.get("comments") # ملاحظات
    
    
    try:
        trumpet = Trumpet.objects.get(trumpet_number=trumpet_number)

        tank = Tank.objects.filter(material= subject_name).last()
        if tank:
                tank.tank_quantity -= float(quantity_sold)
                tank.save()
        else:
            return Response('Sorry No Tank Data :(', status= status.HTTP_400_BAD_REQUEST)
    except Trumpet.DoesNotExist:
        return Response({
            "message": "We couldn't find a trumpet with this number, please make sure its exists or create one"
        }, status=status.HTTP_404_NOT_FOUND)
    
    try:
        ReadingTrumpet.objects.create(
            subject_name = subject_name,
            trumpet_number = trumpet,
            trumpet_caliber = trumpet_caliber,
            receiving_counter = receiving_counter,
            delivery_counter = delivery_counter,
            quantity_sold = quantity_sold,
            price_per_litre = price_per_litre,
            total = total,
            comments = comments
        )
        return Response({
            "message": "Trumpet reading registered successfully!"
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            "message": f"an error occurred while registering the trumpet reading: {e}"
        }, status=status.HTTP_400_BAD_REQUEST)
    
    

@api_view(['POST'])
@permission_classes([permissions.IsAdminUser])
def create_reading_trumpet_k(request):
    try:
        serializer= ReadingTrumpetKSerializer(data= request.data)
        tank = Tank.objects.filter(material= request.data['subject_name']).last()
        if tank:
                tank.tank_quantity -= float(request.data['quantity_sold'])
                tank.save()
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_200_OK)
        else:
            return Response(f'Sorry, there was an error: {error}', status= status.HTTP_400_BAD_REQUEST)
    except Exception as error:
        return Response(f'Sorry, there was an error: {error}', status= status.HTTP_400_BAD_REQUEST)
