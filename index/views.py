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


class Faq(TemplateView):
    template_name = 'pages/faq.html'


class HowitWorks(TemplateView):
    template_name = 'pages/how_it_works.html'


class Writers(TemplateView):
    template_name = 'pages/writers.html'


class Reviews(TemplateView):
    template_name = 'pages/review.html'



