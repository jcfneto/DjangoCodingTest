from django.contrib import admin
from django.urls import path, include

from core.urls import router


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
    path('user/', include('user.urls')),
    path('', include(router.urls))
]

admin.site.site_header = 'IGS - Employee Software Manager'
admin.site.site_title = 'IGS'
admin.site.index_title = 'IGS'
