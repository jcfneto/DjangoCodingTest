from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from django.shortcuts import redirect

from .models import Employee
from .serializers import EmployeeSerializer


def index_view(request):
    return redirect('/admin')


class EmployeeViewSet(viewsets.ModelViewSet):

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'text': 'Employee deleted.'}, status=status.HTTP_200_OK)
