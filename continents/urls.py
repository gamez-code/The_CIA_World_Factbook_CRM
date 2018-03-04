from django.urls import path
from continents.views import ContinentsView, ContinentsDetailIDView, ContinentsEachOneView

app_name = "continents"

urlpatterns = [
    path("", ContinentsView.as_view(), name="home"),
    path("<int:id>/", ContinentsDetailIDView.as_view(), name="continents_id_detail"),
    path("each_one/", ContinentsEachOneView.as_view(), name="each"),
]