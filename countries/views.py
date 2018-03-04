from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from countries.models import Country

class HomeView(TemplateView):
    template_name = 'countries/home.html'

class TagsView(TemplateView):
    template_name = 'countries/tags.html'

class CountryDetailView(TemplateView):
    template_name  = 'countries/country_detail.html'
    def get_context_data(self, *args, **kwargs):
        code = kwargs['code']
        return {'code': code}

class CountryDetailIDView(TemplateView):
    template_name  = 'countries/country_id_detail.html'
    def get_context_data(self, *args, **kwargs):
        code_id = kwargs['id']
        return {'code_id': code_id}

class CountrySearchView(ListView):
    template_name = 'countries/search.html'
    model = Country

    def get_queryset(self):
        type_ = self.kwargs['type']
        query_ = self.kwargs['query']

        if type_ == 'contains':
            return Country.objects.filter(name__contains=query_)
        elif type_ == 'icontains':
            return Country.objects.filter(name__icontains=query_)
        elif type == 'start':
            return Country.objects.filter(name__startswith=query_)
        else:
            return Country.objects.filter(name=query_)


