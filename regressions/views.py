from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.renderers import JSONRenderer
from .models import Run

def latest(request):
    latest = Run.objects.order_by('-id')[:1]
    response = JsonResponse(latest.values()[0])
    return response
