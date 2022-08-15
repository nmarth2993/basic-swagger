from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework import serializers, viewsets
from rest_framework.views import APIView
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer

# Create your views here.


class TestView(APIView):
    def get(self, request, id: str = None):
        if id is None:
            return JsonResponse({'status': 200, 'message': 'OK'})
        else:
            return JsonResponse({'status': 200, 'message': 'OK', 'id': id})
