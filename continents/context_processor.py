from continents.models import Continent
def continents_data(request):
    continents = Continent.objects.all()
    return {'continents': continents}