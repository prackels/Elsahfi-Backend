from rest_framework import serializers
from ..models import BasicInformationAboutTheStation, BranchesInformation, ShiftDetails


class BasicInformationAboutTheStationSerializers(serializers.ModelSerializer):
    class Meta:
        model = BasicInformationAboutTheStation
        fields = "__all__"
class BranchesInformationSerializer(serializers.ModelSerializer) :

    class Meta:
        model = BranchesInformation
        fields = "__all__"

class ShiftDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model= ShiftDetails
        fields= "__all__"