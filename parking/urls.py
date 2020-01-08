from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_address, name="get_address"),
]
