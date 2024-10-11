from rest_framework import serializers
from django.db.models import Sum

from . import models


class EmployeeSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для работы с Сотрудниками
    """
    class Meta:
        model = models.Employee
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для работы с Департаментами
    """
    employees_count = serializers.SerializerMethodField()
    employees_salary = serializers.SerializerMethodField()

    class Meta:
        model = models.Department
        fields = '__all__'

    def get_employees_count(self, obj):
        return models.Employee.objects.filter(department=obj.pk).count()

    def get_employees_salary(self, obj):
        return models.Employee.objects.filter(department=obj.pk).aggregate(Sum('salary'))
