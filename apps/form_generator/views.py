from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class StaticGenerateFV(TemplateView):
    template_name = 'form_generator/static_generate_view.html'
