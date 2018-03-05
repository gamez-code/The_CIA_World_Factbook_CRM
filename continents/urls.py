from django.urls import path
from continents.views import (ContinentsView,
                              ContinentsDetailIDView,
                              ContinentsEachOneView,
                              ContinentsSearchView)

app_name = "continents"

urlpatterns = [
    path("", ContinentsView.as_view(), name="home"),
    path("<int:pk>/", ContinentsDetailIDView.as_view(), name="continents_id_detail"),
    path("each_one/", ContinentsEachOneView.as_view(), name="each"),
    path("each_one/<type>/<query>/",ContinentsSearchView.as_view(), name="search")
]