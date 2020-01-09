from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_address, name="parking_index"),
    path("thanks/", views.get_address),
]
