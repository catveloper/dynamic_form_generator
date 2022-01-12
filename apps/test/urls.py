from django.urls import path

from apps.test.views import StaticGenerateFV

app_name = 'test'

urlpatterns = [
    path('static/<str:view_type>', StaticGenerateFV.as_view(), name='static'),
]


