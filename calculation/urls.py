from django.urls import path
from .views import CalculationView

urlpatterns = [
    path('add/', CalculationView.as_view({'post': 'add'})),
    path('add_by_1/', CalculationView.as_view({'post': 'add_by_1'})),
    path('multiply/', CalculationView.as_view({'post': 'multiply'})),
]