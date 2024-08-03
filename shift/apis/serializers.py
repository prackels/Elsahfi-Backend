from rest_framework import serializers
from shift.models import Shift


class ShiftSerializer (serializers.ModelSerializer) : 
    
    class Meta :
        model = Shift
        fields = '__all__'
    def validate(self, value):
        if Shift.objects.filter(is_active=True).exists() : 
            raise serializers.ValidationError(detail={'message':"there is already active shift"})
        return value
    
    def get_uid (self) -> dict:
        shift = Shift.objects.get(is_active=True)
        return {
            'uid' : shift.uid,
            'shift_time': shift.shift_time
        }