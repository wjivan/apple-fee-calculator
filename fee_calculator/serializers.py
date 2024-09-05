# fee_calculator/serializers.py
from rest_framework import serializers

class FeeCalculatorSerializer(serializers.Serializer):
    annual_revenue = serializers.FloatField(min_value=0)
    total_installs = serializers.IntegerField(min_value=0)
    is_small_business = serializers.BooleanField()
    global_revenue = serializers.FloatField(min_value=0)
    third_party_commission_rate = serializers.FloatField(min_value=0, max_value=100)
    apple_revenue_percentage = serializers.FloatField(min_value=0, max_value=100)