from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response


# Create your views here.
class CalculationView(viewsets.ViewSet):
    @staticmethod
    def add(request):
        first = request.data.get("first")
        second = request.data.get("second")
        return Response({"result": first + second})
