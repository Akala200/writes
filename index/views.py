from django.views.generic import TemplateView
from django.db.models import Max
from django.contrib.auth import get_user_model
from django.shortcuts import render

from writers.models import WritersProfile, Rating



class IndexView(TemplateView):
    template_name = 'index.html'
    model = 'gugu'


