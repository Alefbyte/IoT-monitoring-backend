from django.contrib import admin
from django.urls import path, include
from django_openapi import OpenAPI
from django_openapi import Path, Query, Form
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

api = OpenAPI(title='My OpenAPI Test',	prefix_path='/test_api')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/metrics/', include("metrics.urls")),
    api.as_django_url_pattern(),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]


