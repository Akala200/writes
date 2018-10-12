import json

from django.views.generic import TemplateView
from django.db.models import Max
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_list_or_404
from django.http  import JsonResponse
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.exceptions import ObjectDoesNotExist


from writers.models import WritersProfile, Rating




class IndexView(TemplateView):
    template_name = 'index.html'


class Faq(TemplateView):
    template_name = 'pages/global/faq.html'


class HowitWorks(TemplateView):
    template_name = 'pages/global/how_it_works.html'


class Writers(TemplateView):
    template_name = 'pages/global/writers.html'


class Reviews(TemplateView):
    template_name = 'pages/global/review.html'


class ServicesCustomEssay(TemplateView):
    template_name = 'pages/global/services_customessay.html'

    
class ServicesDissatationWriting(TemplateView):
    template_name = 'pages/global/services_dissatationwriting.html'


class ServicesEssayWriting(TemplateView):
    template_name = 'pages/global/services_essaywriting.html'


class ServicesResearch(TemplateView):
    template_name = 'pages/global/services_research.html'


class ServicesAdmissionEssay(TemplateView):
    template_name = 'pages/global/services_admission_essay.html'

class ServicesCustomWriting(TemplateView):
    template_name = 'pages/global/services_custom_essay.html'

class Services(TemplateView):
    template_name = ''

class ServicesTermPaper(TemplateView):
    template_name = 'pages/global/services_term_paper.html'


class ServicesWriteMyEssay(TemplateView):
    template_name = 'pages/global/services_write_my_essay.html'



class About(TemplateView):
    template_name = 'pages/global/about.html'

class WriterView(TemplateView):
    template_name = 'writers/writers.html'

class Blog(TemplateView):
    template_name = 'pages/blog.html'


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'index/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        page = self.request.GET.get("page", 1)
        try:
            self.request.user.user_profile.is_writer
        except ObjectDoesNotExist:
            from customer.models import Order
            order = Order.objects.filter(order_id=self.request.user).all()

            paginate = Paginator(order, 10)
            try:
                context['orders'] = paginate.page(page)
            except PageNotAnInteger:
                context['orders'] = paginate.page(1)
            except EmptyPage:
                context['orders'] = paginate.page(paginate.num_pages)
            for query in order:
                context['offers'] = query.offer_id.offers
            
        else:
            from writers.models import WritersProfile
            context['writers'] = WritersProfile.objects.all()

            

           
        return context








