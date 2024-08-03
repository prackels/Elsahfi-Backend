from rest_framework import serializers
from ..models import PaymentOfTheDeadLine, ShiftCash, Cash

class PaymentOfTheDeadlineSerializer(serializers.ModelSerializer):
    def format_time(self, instance):
        return instance.time.strftime("%I:%M %p")
    time= serializers.SerializerMethodField(method_name='format_time')
    class Meta:
        model= PaymentOfTheDeadLine
        fields= '__all__'

class CashSerializer(serializers.ModelSerializer):
    class Meta:
        model= Cash
        fields= '__all__'
class ShiftCashSerializer(serializers.ModelSerializer):
    def format_time(self, instance):
        return instance.time.strftime("%I:%M %p")
    time= serializers.SerializerMethodField(method_name='format_time')
    class Meta:
        model= ShiftCash
        fields= '__all__'