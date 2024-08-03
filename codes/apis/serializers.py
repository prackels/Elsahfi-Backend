from rest_framework import serializers
from ..models import Code, EncryptedCodes,EmployeesCodes

class EncryptedCodesSerializer(serializers.ModelSerializer):
    class Meta:
        model= EncryptedCodes
        fields= '__all__'

class CodeSerializer(serializers.ModelSerializer):
    class Meta:
        model= Code
        fields= '__all__'

class EmployeesCodesSerializer(serializers.ModelSerializer):
    class Meta:
        model= EmployeesCodes
        fields= '__all__'
