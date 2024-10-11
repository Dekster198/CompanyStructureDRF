from django.urls import path, include
from rest_framework import routers
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

from . import views


router = routers.SimpleRouter()
router.register(r'employee', views.EmployeeViewSet)
router.register(r'department', views.DepartmentViewSet)

urlpatterns = [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include(router.urls)),
    path('api/v1/', include(router.urls)),
]
