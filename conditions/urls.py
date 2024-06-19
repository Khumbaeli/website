from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:location_id>/results/", views.detail, name="locations"),
]