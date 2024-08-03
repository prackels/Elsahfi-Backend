from django.core.cache import cache
from rest_framework import serializers
from ..models import Trumpet, ReadingTrumpet, ReadingTrumpet_K

class TrumpetSerializer(serializers.ModelSerializer):
    # def format_date(self, instance):
    #     return instance.date.strftime("%Y-%m-%d")
    # def format_time(self, instance):
    #     return instance.time.strftime("%I:%M %p")
    # date= serializers.SerializerMethodField(method_name='format_date')
    # time= serializers.SerializerMethodField(method_name='format_time')
    class Meta:
        model = Trumpet
        fields = '__all__'
class ReadingTrumpetSerializer(serializers.ModelSerializer):
    def format_date(self, instance):
        return instance.date.strftime("%Y-%m-%d")
    def format_time(self, instance):
        return instance.time.strftime("%I:%M %p")
    date= serializers.SerializerMethodField(method_name='format_date')
    time= serializers.SerializerMethodField(method_name='format_time')
    class Meta:
        model= ReadingTrumpet
        fields= '__all__'

class AnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model= ReadingTrumpet
        fields= '__all__'

class ReadingTrumpetKSerializer(serializers.ModelSerializer):
    def format_date(self, instance):
        return instance.date.strftime("%Y-%m-%d")
    def format_time(self, instance):
        return instance.time.strftime("%I:%M %p")
    date= serializers.SerializerMethodField(method_name='format_date')
    time= serializers.SerializerMethodField(method_name='format_time')
    class Meta:
        model= ReadingTrumpet_K
        fields= '__all__'

