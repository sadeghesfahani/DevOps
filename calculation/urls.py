from django.urls import path
from .views import CalculationView

urlpatterns = [
    path('add/', CalculationView.as_view({'post': 'add'})),
]