from django.shortcuts import render
from django.views.generic import (TemplateView,)
from django.views.generic.list import ListView
from countries.models import Country
# Create your views here.
class ContinentsView(TemplateView):
    template_name = "continents/continents.html"
    """
        def get_context_data(self,*args,**kwargs):

        return {'continents': continents}
    """
class ContinentsDetailIDView(TemplateView):
    template_name = "continents/continents_detail.html"
    def get_context_data(self, *args, **kwargs):
        id = kwargs['id']
        return {'id': id}

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

        if type_ == 'contains':
            return Country.objects.filter(name__contains=query_ )
        elif type_ == 'icontains':
            return Country.objects.filter(name__icontains=query_)
        elif type == 'start':
            return Country.objects.filter(name__startswith=query_)
        else:
            return Country.objects.filter(name=query_)
