from django.urls import path
from countries.views import ( CountryDetailView, CountryDetailIDView,
CountrySearchView )

app_name = 'countries'

urlpatterns = [
    path("search/<type>/<query>/", CountrySearchView.as_view(),name="country_search"),
    path("<int:id>/", CountryDetailIDView.as_view(), name="country_id_detail"),
    path("<code>/", CountryDetailView.as_view(), name="country_code_detail"),
    ]