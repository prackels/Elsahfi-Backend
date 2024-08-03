from ..models import NewPurchase, NewSupplier
from rest_framework import serializers


class NewPurchaseSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        data= super().to_representation(instance)
        data["order_time"] = instance.order_time.strftime("%I:%M %p")
        data["time"] = instance.order_time.strftime("%I:%M %p")
        data["time_to_go_out"]= instance.order_time.strftime("%I:%M %p")
        data["entry_time"]= instance.order_time.strftime("%I:%M %p")

        return data
    
    class Meta:
        model = NewPurchase
        fields = '__all__'



class NewSupplierSerializer(serializers.ModelSerializer):
    def format_time(self, instance):
        return instance.time.strftime("%I:%M %p")
    time= serializers.SerializerMethodField(method_name='format_time')
    class Meta:
        model= NewSupplier
        fields= '__all__'

