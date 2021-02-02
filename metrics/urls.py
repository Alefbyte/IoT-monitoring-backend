from django.urls import path
from drf_spectacular.views import SpectacularAPIView
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()

router.register('sensor-types', SensorTypeViewSet)
router.register('sensors', SensorsViewSet, basename='sensors')
router.register('log', LogViewSet, basename='log')
# path('api/schema/', SpectacularAPIView.as_view(), name='schema')


urlpatterns = [
]

urlpatterns += router.urls
