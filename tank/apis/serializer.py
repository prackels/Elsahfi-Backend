from rest_framework import serializers
from ..models import Tank
from trumpet.models import Trumpet
from trumpet.apis.serializers import TrumpetSerializer

class TankSerializer (serializers.ModelSerializer) : 
    trumpets = serializers.SerializerMethodField()
    class Meta :
        model = Tank
        fields = '__all__'

    def get_trumpets(self, obj):
        trumpets = Trumpet.objects.filter(tank__id=obj.id)
        serializer = TrumpetSerializer(trumpets, many=True)
        return serializer.data
class TankSpecificUpdates (serializers.ModelSerializer) :
    class Meta:
        model = Tank
        fields = ('tank_quantity','remaining_quantity','tank_caliber',)