# fee_calculator/urls.py
from django.urls import path
from .views import FeeCalculatorView

urlpatterns = [
    path('', FeeCalculatorView.as_view(), name='fee_calculator'),
]