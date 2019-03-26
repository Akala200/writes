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
    template_name = 'pages/australia/faq.html'


class HowitWorks(TemplateView):
    template_name = 'pages/australia/how_it_works.html'


class Writers(TemplateView):
    template_name = 'pages/australia/writers.html'


class Reviews(TemplateView):
    template_name = 'pages/australia/review.html'


class ServicesCustomEssay(TemplateView):
    template_name = 'pages/australia/services_customessay.html'

    
class ServicesDissatationWriting(TemplateView):
    template_name = 'pages/australia/services_dissatationwriting.html'


class ServicesEssayWriting(TemplateView):
    template_name = 'pages/australia/services_essaywriting.html'


class ServicesResearch(TemplateView):
    template_name = 'pages/australia/services_research.html'


class ServicesAdmissionEssay(TemplateView):
    template_name = 'pages/australia/services_admission_essay.html'

class ServicesCustomWriting(TemplateView):
    template_name = 'pages/australia/services_custom_essay.html'

class Services(TemplateView):
    template_name = ''

class ServicesTermPaper(TemplateView):
    template_name = 'pages/australia/services_term_paper.html'


class ServicesWriteMyEssay(TemplateView):
    template_name = 'pages/australia/services_write_my_essay.html'



class About(TemplateView):
    template_name = 'pages/australia/about.html'





