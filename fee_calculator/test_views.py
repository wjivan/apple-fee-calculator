# fee_calculator/test_views.py
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from decimal import Decimal

class FeeCalculatorViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('fee_calculator')

    def test_fee_calculator_view_success(self):
        data = {
            'annual_revenue': '1000.00',
            'total_installs': 500000,
            'is_small_business': True,
            'global_revenue': '5000000.00',
            'apple_revenue_percentage': '70.00',
            'third_party_commission_rate': '10.00'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('existing_terms', response.data)
        self.assertIn('existing_terms_link_out', response.data)
        self.assertIn('alternative_terms', response.data)
        self.assertIn('alternative_terms_link_out', response.data)
        self.assertIn('most_cost_effective', response.data)

    def test_fee_calculator_view_invalid_data(self):
        data = {
            'annual_revenue': '-1000.00',  # Invalid negative value
            'total_installs': 500000,
            'is_small_business': True,
            'global_revenue': '5000000.00',
            'apple_revenue_percentage': '70.00',
            'third_party_commission_rate': '10.00'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)