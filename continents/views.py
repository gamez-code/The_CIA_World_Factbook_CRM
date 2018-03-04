from django.shortcuts import render
from django.views.generic import TemplateView
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