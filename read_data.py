import json
import random
import django
import os, sys
djangoproject_home = "."
sys.path.append(djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'geographic.settings'
django.setup()
from continents.models import Continent
from countries.models import Country

def f_country():
    countries_file = open("/home/grupo-ari/manuel/practicas/programas/Python/django/geographic/data/factbook.json/countries","r")
    countries = []

    while (True):
        country_ = {}
        _country_ = {"model":"countries.country","fields":{}}
        country = countries_file.readline()
        if country == '':
            break
        elif country[0] == '*':
            continue
        elif country[0] == '`':
            country_['code'], country_['name'] = country.replace('`', '').replace('\n', '').split(' ', maxsplit=1)
            _country_["fields"] = country_
            countries.append(_country_)

    countries_writer = open("/home/grupo-ari/manuel/practicas/programas/Python/django/geographic/countries/fixtures/countries.json","w")
    json.dump(countries, countries_writer)
    countries_writer.close()

def f_continent_country():
    continent_file = open("/home/grupo-ari//manuel/practicas/programas/Python/django/geographic/data/factbook.json/continents_code","r")
    continents = []
    while (True):
        continent_ = {}
        _continent_ = {"model": "continets.continent", "fields": {}}
        continent = continent_file.readline()
        if continent == '':
            break
        elif continent[0] == '.':
            continent_['code'], continent_['name'] = \
                continent.replace('./', '')\
                    .replace('.json', '')\
                    .replace('/', ' ')\
                    .replace('\n', '')\
                    .split(' ', maxsplit=1)
            _continent_["fields"] = continent_
            continents.append(_continent_)

    continents_writer = open(
        "/home/grupo-ari/manuel/practicas/programas/Python/django/geographic/continents/fixtures/continents.json", "w")
    json.dump(continents, continents_writer)
    continents_writer.close()

def f_continent_code():
    continent_file = open("/home/grupo-ari/manuel/practicas/programas/Python/django/geographic/data/factbook.json/continents_code_continents","r")
    continents = []
    r = lambda: random.randint(0, 255)
    while (True):
        continent_ = {}
        _continent_ = {"model": "continents.continent", "fields": {}}
        continent = continent_file.readline()
        if continent == '':
            break
        else:
            continent_['name'],continent_['translation'], continent_['code'] = \
                    continent.replace('\n', '') \
                .split(' ', maxsplit=2)
            continent_['color'] = '#%02X%02X%02X' % (r(),r(),r())
            _continent_["fields"] = continent_
            continents.append(_continent_)

    continents_writer = open(
        "/home/grupo-ari/manuel/practicas/programas/Python/django/geographic/continents/fixtures/continents.json", "w")
    json.dump(continents, continents_writer)
    continents_writer.close()


def f_country_continent_code():
    countries_file = open(
        "/home/grupo-ari//manuel/practicas/programas/Python/django/geographic/data/country_n_continents", "r")
    countries = []
    problem = []
    while (True):
        countries_ = {}
        _countries_ = {"model": "countries.country", "fields": {}}
        country = countries_file.readline()
        if country == '':
            break
        else:
            countries_['continent'],countries_['country'] = \
                    country.replace('.json\n', '') \
                    .replace('./data/factbook.json/', '')\
                    .split('/', maxsplit=1)
            countries_['continent'] = Continent.objects.get(name=countries_['continent']).id
            try:
                countries_db = Country.objects.get(code=countries_['country'])
            except:
                countries_db = Country.objects.get(code__regex=r'^'+countries_['country']+'_.')
            if not countries_db:
                problem.append(countries_db)
                continue
            elif countries_db:
                countries_['country'] = countries_db.id
                print(countries_)
                # _country_["fields"] = continent_
                countries.append(countries_)

    #continents_writer = open(
    #    "/home/grupo-ari/manuel/practicas/programas/Python/django/geographic/continents/fixtures/continents.json", "w")
    #json.dump(continents, continents_writer)
    #continents_writer.close()

#f_country_continent_code()
f_country()