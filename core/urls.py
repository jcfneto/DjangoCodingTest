from rest_framework.routers import DefaultRouter

from core.views import EmployeeViewSet


router = DefaultRouter()
router.register(r'employee', EmployeeViewSet, basename='employee')
