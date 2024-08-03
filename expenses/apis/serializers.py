from rest_framework import serializers
from expenses.models import GovernmentExpense, StationExpense, CarsExpenses
from clients_.apis.serializers import CarsSerializer


class StationExpSerializer (serializers.ModelSerializer) : 
    def format_date(self, instance):
        return instance.date.strftime("%Y-%m-%d")
    def format_time(self, instance):
        return instance.time.strftime("%I:%M %p")
    date= serializers.SerializerMethodField(method_name='format_date')
    time= serializers.SerializerMethodField(method_name='format_time')
    class Meta :
        model = StationExpense
        fields = "__all__"

class GovernmentExpSerializer (serializers.ModelSerializer) : 
    def format_date(self, instance):
        return instance.date.strftime("%Y-%m-%d")
    def format_time(self, instance):
        return instance.time.strftime("%I:%M %p")
    date= serializers.SerializerMethodField(method_name='format_date')
    time= serializers.SerializerMethodField(method_name='format_time')
    class Meta :
        model = GovernmentExpense
        fields = "__all__"

class CarsExpensesSerializer (serializers.ModelSerializer) : 
    def format_date(self, instance):
        return instance.date.strftime("%Y-%m-%d")
    def format_time(self, instance):
        return instance.time.strftime("%I:%M %p")
    date= serializers.SerializerMethodField(method_name='format_date')
    time= serializers.SerializerMethodField(method_name='format_time')
    car_type = serializers.SerializerMethodField(read_only=True)
    class Meta :
        model = CarsExpenses
        fields = "__all__"

    def get_car_type(self, obj):
        return {
            'car_name': obj.car_type.car_name
        }
