from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Run, Test
from regressions.serializers import RunSerializer, TestSerializer
from django.db.models import Count, F, Value

# Run
class RunViewSet(viewsets.ModelViewSet):
    queryset = Run.objects.all()
    serializer_class = RunSerializer

    @action(detail=False)
    def latest(self, request):
        latest_run = Run.objects.order_by('-id')[:1]
        serializer = self.get_serializer(latest_run, many=True)
        return Response(serializer.data)

# Test
class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer