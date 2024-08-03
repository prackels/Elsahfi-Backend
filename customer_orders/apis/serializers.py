from ..models import CustomerStation, TrillaCustomer, DeiannaCustomer
from rest_framework import serializers
from clients_.apis.serializers import NewCustomerSerializer
from clients_.models import NewCustomer
from employee.apis.serializers import CarSerializer


    
class CustomerStationSerializer(serializers.ModelSerializer):
    def format_date(self, instance):
        return instance.date.strftime("%Y-%m-%d")
    def format_time(self, instance):
        return instance.time.strftime("%I:%M %p")
    date= serializers.SerializerMethodField(method_name='format_date')
    time= serializers.SerializerMethodField(method_name='format_time')
    
    class Meta:
        model= CustomerStation
        fields= '__all__'

    def to_representation(self, instance):

        data = super().to_representation(instance)        
        
        query = NewCustomer.objects.filter(customer_name=instance.customer_name)
        data['client'] = NewCustomerSerializer(query,many=True).data

        return data


class TrillaCustomerSerializer(serializers.ModelSerializer):
    def format_date(self, instance):
        return instance.date.strftime("%Y-%m-%d")
    def format_time(self, instance):
        return instance.time.strftime("%I:%M %p")
    date= serializers.SerializerMethodField(method_name='format_date')
    time= serializers.SerializerMethodField(method_name='format_time')
    car_type = CarSerializer(read_only=True, many=False)
    class Meta:
        model= TrillaCustomer
        fields= '__all__'

    def to_representation(self, instance):

        data = super().to_representation(instance)        
        
        query = NewCustomer.objects.filter(customer_name=instance.customer_name)
        data['client'] = NewCustomerSerializer(query,many=True).data

        return data

class DeiannaCustomerSerializer(serializers.ModelSerializer):
    def format_date(self, instance):
        return instance.date.strftime("%Y-%m-%d")
    def format_time(self, instance):
        return instance.time.strftime("%I:%M %p")
    date= serializers.SerializerMethodField(method_name='format_date')
    time= serializers.SerializerMethodField(method_name='format_time')
    car_type = CarSerializer(read_only=True, many=False)

    class Meta:
        model= DeiannaCustomer
        fields= '__all__'


    def to_representation(self, instance):

        data = super().to_representation(instance)        
        
        query = NewCustomer.objects.filter(customer_name=instance.customer_name)
        data['client'] = NewCustomerSerializer(query,many=True).data

        return data