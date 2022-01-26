from django.contrib import admin
from django.urls import path, include

from core.urls import router
from core.views import index_view

urlpatterns = [
    path('', index_view, name='index'),
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls'))
]

admin.site.site_header = 'IGS - Employee Software Manager'
admin.site.site_title = 'IGS'
admin.site.index_title = 'IGS'
