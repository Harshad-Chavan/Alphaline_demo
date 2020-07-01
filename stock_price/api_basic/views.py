from django.shortcuts import render,HttpResponse
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import PriceSerializer
from .scrapper3 import compute_price
# Create your views here.
class TaskViewSet(viewsets.ViewSet):
    # Required for the Browsable API renderer to have a nice form.
    serializer_class = PriceSerializer

    def list(self, request):
        security = compute_price()
        serializer = PriceSerializer(
            instance=security.values(), many=True)
        return Response(serializer.data)