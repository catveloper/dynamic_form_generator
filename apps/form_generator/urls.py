from django.urls import path

from apps.form_generator.views import StaticGenerateFV

app_name = 'form_generator'

urlpatterns = [
    path('static/', StaticGenerateFV.as_view(), name='static')
]