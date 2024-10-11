from rest_framework import generics, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from .models import *
from . import serializers


# Create your views here.
class EmployeePagination(PageNumberPagination):
    """
    Пагинация для Сотрудников
    """
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class EmployeeViewSet(viewsets.ModelViewSet):
    """
    ViewSet для работы с Сотрудниками
    """
    queryset = Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'fio']
    pagination_class = EmployeePagination
    permission_classes = [IsAuthenticated]


class DepartmentViewSet(viewsets.ModelViewSet):
    """
    ViewSet для работы с Департаментами
    """
    queryset = Department.objects.all()
    serializer_class = serializers.DepartmentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
