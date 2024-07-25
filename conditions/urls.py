from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('delete_forecast/<int:index>/', views.delete_forecast, name='delete_forecast'),
]