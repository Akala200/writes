from django.views.generic import ListView, DetailView, DeleteView
from django.http import HttpResponseBadRequest
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Article


class ArticleListing(ListView):
     template_name = ''
     paginate_by = 10
     context_object_name = 'article'
     model = Article


class ArticleDetail(DetailView):
    template_name = ''
    slug_url_kwarg = 'artice_id'
    context_object_name = 'article'
    model = Article

    def get_context_data(self):
        pass

class DeleteArticle(LoginRequiredMixin, DeleteView):
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff or request.user.is_admin:
            return HttpResponseBadRequest('You are not allowed to delete these items')
        return super(DeleteArticle, self).dispatch(request, *args, **kwargs)




    
