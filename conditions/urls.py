from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('forecast_actions/<int:index>/', views.forecast_actions, name='forecast_actions'),
    
]