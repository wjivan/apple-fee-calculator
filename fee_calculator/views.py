from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import FeeCalculatorSerializer
from .calculations import calculate_fees, generate_chart
import pdb

class FeeCalculatorView(APIView):
    def get(self, request):
        return render(request, 'fee_calculator/calculator.html')

    def post(self, request):
        serializer = FeeCalculatorSerializer(data=request.data)
        if serializer.is_valid():
            results = calculate_fees(**serializer.validated_data)
            chart_image = generate_chart(results)
            return render(request, 'fee_calculator/results.html', {
                'results': results,
                'chart_image': chart_image
            })
        return Response(serializer.errors, status=400)