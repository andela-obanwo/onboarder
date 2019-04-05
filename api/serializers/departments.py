from rest_framework import serializers

from api.models import Departments


class DepartmentSerializer(serializers.ModelSerializer):

     class Meta:
        model = Departments
        fields = '__all__'