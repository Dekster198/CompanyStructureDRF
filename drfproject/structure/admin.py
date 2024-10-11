from django.contrib import admin

from .models import *


# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'fio', 'photo', 'post', 'salary', 'age', 'department']
    list_display_links = ['id', 'fio']
    ordering = ['fio']
    list_editable = ['salary', 'age']
    list_per_page = 10
    search_fields = ['fio', 'post', 'salary', 'age', 'department__title']
    list_filter = ['fio', 'post', 'department__title']


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'email']
    list_display_links = ['id', 'title']
    ordering = ['title']
    list_per_page = 10
    search_fields = ['title']
