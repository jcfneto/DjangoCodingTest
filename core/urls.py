from rest_framework.routers import DefaultRouter
from core.views import DepartmentViewSet, EmployeeViewSet


router = DefaultRouter()
router.register(r'employee', viewset=EmployeeViewSet, basename='employee')
router.register(r'department', viewset=DepartmentViewSet, basename='department')

urlpatterns = router.urls
