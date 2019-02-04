from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework import viewsets
from .models import Run, Test
from regressions.serializers import RunSerializer, TestSerializer

# Run
class RunViewSet(viewsets.ModelViewSet):
    queryset = Run.objects.all()
    serializer_class = RunSerializer

def latest(request):
    latest = Run.objects.order_by('-id')[:1]
    response = JsonResponse(latest.values()[0])
    return response

# Test
class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer