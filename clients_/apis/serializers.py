from rest_framework import serializers
from ..models import *

class NewCustomerSerializer(serializers.ModelSerializer):
    # def format_date(self, instance):
    #     return instance.date.strftime("%Y-%m-%d")
    # def format_time(self, instance):
    #     return instance.time.strftime("%I:%M %p")
    # date= serializers.SerializerMethodField(method_name='format_date')
    # time= serializers.SerializerMethodField(method_name='format_time')
    class Meta:
        model= NewCustomer
        fields= '__all__'

class CarsSerializer(serializers.ModelSerializer):
    # customer = NewCustomerSerializer(read_only=True, many=False)
    class Meta:
        model= Cars
        fields= '__all__'

class CustomersCarsSerializer(serializers.ModelSerializer):
    customer = NewCustomerSerializer(read_only=True, many=False)
    class Meta:
        model= Cars
        fields= '__all__'

class SubjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model= Subjects
        fields= '__all__'

class CustomersSubjectsSerializer(serializers.ModelSerializer):
    customer = NewCustomerSerializer(read_only=True, many=False)

    class Meta:
        model= Subjects
        fields= '__all__'