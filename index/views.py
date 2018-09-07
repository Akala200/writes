import json

from django.views.generic import TemplateView
from django.db.models import Max
from django.contrib.auth import get_user_model
from django.shortcuts import render, get_list_or_404
from django.http  import JsonResponse
from django.core import serializers

from writers.models import WritersProfile, Rating





class IndexView(TemplateView):
    template_name = 'index.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rating'] = get_list_or_404(get_user_model())
        return context


