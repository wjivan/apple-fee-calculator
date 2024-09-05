# fee_calculator/test_calculations.py
from django.test import TestCase
from .calculations import (
    calculate_existing_terms,
    calculate_existing_terms_link_out,
    calculate_alternative_terms,
    calculate_alternative_terms_link_out,
    calculate_ctf,
    calculate_fees
)

class CalculationTestCase(TestCase):
    def test_calculate_existing_terms(self):
        self.assertEqual(calculate_existing_terms(1000, True), 150)  # Small business
        self.assertEqual(calculate_existing_terms(1000, False), 300)  # Standard

    def test_calculate_existing_terms_link_out(self):
        self.assertEqual(calculate_existing_terms_link_out(1000, True), 120)  # Small business
        self.assertEqual(calculate_existing_terms_link_out(1000, False), 250)  # Standard

    def test_calculate_alternative_terms(self):
        result = calculate_alternative_terms(
            annual_revenue=1000,
            total_installs=500000,
            is_small_business=True,
            global_revenue=5000000,
            apple_revenue_percentage=0.7,
            third_party_commission_rate=10
        )
        self.assertAlmostEqual(result, 121)  # 91 (Apple) + 30 (3rd party) + 0 (CTF)

    def test_calculate_alternative_terms_link_out(self):
        result = calculate_alternative_terms_link_out(
            annual_revenue=1000,
            total_installs=500000,
            is_small_business=True,
            global_revenue=5000000,
            apple_revenue_percentage=0.7,
            third_party_commission_rate=10
        )
        self.assertAlmostEqual(result, 100)  # 70 (Apple) + 30 (3rd party) + 0 (CTF)

    def test_calculate_ctf(self):
        self.assertEqual(calculate_ctf(500000, 5000000), 0)  # Below €10M, exempt
        self.assertEqual(calculate_ctf(2000000, 20000000), 500000)  # Between €10M and €50M
        self.assertEqual(calculate_ctf(3000000, 60000000), 1000000)  # Over €50M

    def test_calculate_fees(self):
        result = calculate_fees(
            annual_revenue=1000,
            total_installs=500000,
            is_small_business=True,
            global_revenue=5000000,
            apple_revenue_percentage=0.7,
            third_party_commission_rate=10
        )
        self.assertIn('existing_terms', result)
        self.assertIn('existing_terms_link_out', result)
        self.assertIn('alternative_terms', result)
        self.assertIn('alternative_terms_link_out', result)
        self.assertIn('most_cost_effective', result)