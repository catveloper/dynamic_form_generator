from django.urls import path, include
from drf_spectacular.views import SpectacularJSONAPIView, SpectacularAPIView, SpectacularSwaggerView, \
    SpectacularRedocView
from rest_framework import routers

from api.viewset import *

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'users', viewset=UserViewSet)
router.register(r'groups', viewset=GroupViewSet)
router.register(r'custom_users', viewset=CustomUserViewSet)

# Auto Generate API
urlpatterns = [
    path('', include(router.urls)),
]

# Custom API
urlpatterns += [
    path('form_generate/static/', StaticFormGeneratorAPI.as_view(), name='static_form_schema'),
]

# Spectacular Document API
urlpatterns += [
    path("docs/json/", SpectacularJSONAPIView.as_view(), name="schema-json"),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/user', SpectacularAPIView.as_view(), name='user_schema'),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='api:schema'), name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='api:schema'), name='redoc'),
]