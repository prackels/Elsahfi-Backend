from ..models import *
from rest_framework import serializers
from shift.apis.serializers import ShiftSerializer

class StationCustomerInvoiceSerializer(serializers.ModelSerializer):
    def format_date(self, instance):
        return instance.date.strftime("%Y-%m-%d")
    def format_time(self, instance):
        return instance.time.strftime("%I:%M %p")
    date= serializers.SerializerMethodField(method_name='format_date')
    time= serializers.SerializerMethodField(method_name='format_time')
    shift = ShiftSerializer(read_only=True, many=False)
    class Meta:
        model= StationCustomerInvoice
        fields= '__all__'

class TrillaCustomersSerializer(serializers.ModelSerializer):
    def format_date(self, instance):
        return instance.date.strftime("%Y-%m-%d")
    def format_time(self, instance):
        return instance.time.strftime("%I:%M %p")
    date= serializers.SerializerMethodField(method_name='format_date')
    time= serializers.SerializerMethodField(method_name='format_time')
    shift = ShiftSerializer(read_only=True, many=False)

    class Meta:
        model= TrillaCustomers
        fields= '__all__'


class NewPurchasingClientsInvoiceSerializer(serializers.ModelSerializer):
    def format_date(self, instance):
        return instance.date.strftime("%Y-%m-%d")
    def format_time(self, instance):
        return instance.time.strftime("%I:%M %p")
    date= serializers.SerializerMethodField(method_name='format_date')
    time= serializers.SerializerMethodField(method_name='format_time')
    # shift = ShiftSerializer(read_only=True, many=False)

    class Meta:
        model= NewPurchasingClientsInvoice
        fields= '__all__'


class DeiannaCustomerInvoiceSerializer(serializers.ModelSerializer):
    def format_date(self, instance):
        return instance.date.strftime("%Y-%m-%d")
    def format_time(self, instance):
        return instance.time.strftime("%I:%M %p")
    date= serializers.SerializerMethodField(method_name='format_date')
    time= serializers.SerializerMethodField(method_name='format_time')
    shift = ShiftSerializer(read_only=True, many=False)

    class Meta:
        model= DeiannaCustomerInvoice
        fields= '__all__'

class StationExpenseInvoiceSerializer(serializers.ModelSerializer):
    def format_date(self, instance):
        return instance.date.strftime("%Y-%m-%d")
    def format_time(self, instance):
        return instance.time.strftime("%I:%M %p")
    date= serializers.SerializerMethodField(method_name='format_date')
    time= serializers.SerializerMethodField(method_name='format_time')
    # shift = ShiftSerializer(read_only=True, many=False)

    class Meta:
        model= StationExpenseInvoice
        fields= '__all__'

class GovernmentExpensesInvoiceSerializer(serializers.ModelSerializer):
    def format_date(self, instance):
        return instance.date.strftime("%Y-%m-%d")
    def format_time(self, instance):
        return instance.time.strftime("%I:%M %p")
    date= serializers.SerializerMethodField(method_name='format_date')
    time= serializers.SerializerMethodField(method_name='format_time')
    # shift = ShiftSerializer(read_only=True, many=False)

    class Meta:
        model= GovernmentExpensesInvoice
        fields= '__all__'


class OfficialPapersOfEmployeesInvoiceSerializer(serializers.ModelSerializer):
    def format_date(self, instance):
        return instance.date.strftime("%Y-%m-%d")
    def format_time(self, instance):
        return instance.time.strftime("%I:%M %p")
    date= serializers.SerializerMethodField(method_name='format_date')
    time= serializers.SerializerMethodField(method_name='format_time')
    # shift = ShiftSerializer(read_only=True, many=False)

    class Meta:
        model= OfficialPapersOfEmployeesInvoice
        fields= '__all__'

class DepositCashToTheStationSerializer(serializers.ModelSerializer):
    def format_date(self, instance):
        return instance.date.strftime("%Y-%m-%d")
    def format_time(self, instance):
        return instance.time.strftime("%I:%M %p")
    date= serializers.SerializerMethodField(method_name='format_date')
    time= serializers.SerializerMethodField(method_name='format_time')
    # shift = ShiftSerializer(read_only=True, many=False)

    class Meta:
        model= DepositCashToTheStation
        fields= '__all__'
