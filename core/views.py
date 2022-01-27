from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from django.shortcuts import redirect

from .models import Department, Employee
from .serializers import DepartmentSerializer, EmployeeSerializer


def index_view(request):
    return redirect('/admin')


class DepartmentViewSet(viewsets.ModelViewSet):

    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'text': 'Department deleted.'}, status=status.HTTP_200_OK)


class EmployeeViewSet(viewsets.ModelViewSet):

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'text': 'Employee deleted.'}, status=status.HTTP_200_OK)
