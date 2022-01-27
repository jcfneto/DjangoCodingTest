from django.contrib import admin

from .models import Department, Employee


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'created_at')


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'email', 'department')
