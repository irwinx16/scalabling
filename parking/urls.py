from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_address),
    path("thanks/", views.get_address),
]
