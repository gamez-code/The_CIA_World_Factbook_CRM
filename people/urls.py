from django.urls import path, include
from people.views import register

app_name = "people"

urlpatterns = [
    path("register/", register, name="register")
]