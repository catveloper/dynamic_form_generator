from django.urls import path, include
from drf_spectacular.views import SpectacularJSONAPIView, SpectacularAPIView, SpectacularSwaggerView, \
    SpectacularRedocView
from rest_framework import routers

from api.views import *

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'users', viewset=UserViewSet)
router.register(r'groups', viewset=GroupViewSet)

urlpatterns = [
    # Auto Generate API
    path('', include(router.urls)),

    # Custom API
    path('form_generate/', FormGeneratorAPI.as_view()),
]
