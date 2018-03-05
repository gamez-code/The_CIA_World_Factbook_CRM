from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.views.generic import (TemplateView,)
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from countries.models import Country
from continents.models import Continent
# Create your views here.
class ContinentsView(TemplateView):
    template_name = "continents/continents.html"
    """
        def get_context_data(self,*args,**kwargs):

        return {'continents': continents}
    """
class ContinentsDetailIDView(DetailView):
    template_name = "continents/continents_detail.html"
    model = Continent

class ContinentsEachOneView(TemplateView):
    template_name = "continents/continents_countries.html"
    """
        def get_context_data(self,*args,**kwargs):

        return {'continents': continents}
    """
class ContinentsSearchView(ListView):
    template_name = 'continents/search.html'
    model = Country

    def get_queryset(self):
        type_ = self.kwargs['type']
        query_ = self.kwargs['query']
        try:
            if type_ == 'contains':
                return Country.objects.filter(name__contains=query_ )
            elif type_ == 'icontains':
                return Country.objects.filter(name__icontains=query_)
            elif type == 'start':
                return Country.objects.filter(name__startswith=query_)
            else:
                return Country.objects.filter(name=query_)
        except Country.DoesNotExist as e:
            raise Http404()
