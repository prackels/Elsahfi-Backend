from rest_framework import serializers
from ..models import Employee, Car



class EmployeeSerializer (serializers.ModelSerializer) : 
    def format_date(self, instance):
        return instance.date.strftime("%Y-%m-%d")
    def format_time(self, instance):
        return instance.time.strftime("%I:%M %p")
    date= serializers.SerializerMethodField(method_name='format_date')
    time= serializers.SerializerMethodField(method_name='format_time')
    class Meta : 
        model = Employee
        fields = '__all__'

class CarSerializer (serializers.ModelSerializer) :
    def format_date(self, instance):
        return instance.date.strftime("%Y-%m-%d")
    def format_time(self, instance):
        return instance.time.strftime("%I:%M %p")
    date= serializers.SerializerMethodField(method_name='format_date')
    time= serializers.SerializerMethodField(method_name='format_time') 
    class Meta : 
        model = Car
        fields = '__all__'