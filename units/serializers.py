from rest_framework import serializers
from .models import DepartmentalUnit

class DepartmentalUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartmentalUnit
        fields = ['id', 'name', 'code']