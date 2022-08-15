"""swagger_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import include, path


from rest_framework import routers, serializers, viewsets, renderers, schemas

from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.views import APIView
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer


# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)


"""
schema_view = get_schema_view(title='Users API', renderer_classes=[
                              OpenAPIRenderer, SwaggerUIRenderer, renderers.CoreJSONRenderer])
"""

# XXX main guide:
# https://github.com/marcgibbons/django-rest-swagger/issues/547

# XXX then
# https://stackoverflow.com/questions/57654243/how-to-fix-attributeerror-at-api-doc-autoschema-object-has-no-attribute-ge

# XXX then `Cannot return a coreapi object from a JSON view. You should be using a schema renderer instead for this view`
# so JSON renderers were removed from settings.py

# XXX then `'rest_framework' is not a registered namespace`
# so changed to include(router.urls, namespace='rest_framework')
# https://stackoverflow.com/questions/28044219/urest-framework-is-not-a-registered-namespace

# XXX then ImproperlyConfiguredError, must use app name when using namespace in include
# so pass 2-tuple of app name
# https://stackoverflow.com/questions/48608894/improperlyconfigurederror-about-app-name-when-using-namespace-in-include

# XXX make this api view to take a request and return a response


# NOTE: the renderer classes decorator is very important so that it only tries to render requests of the correct type.
# cannot render json and will fail with a runtime error: expected coreapi document

@api_view()
@renderer_classes([renderers.CoreJSONRenderer, OpenAPIRenderer, SwaggerUIRenderer])
def schema_view(request):
    generator = schemas.SchemaGenerator(title='TEST')
    document = generator.get_schema(request=request)
    print(document)
    return Response(document)


# router.register(r'test', TestView.as_view())
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', schema_view),
    # XXX must pass a 2-tuple of url map and app name to include() since we defined a namespace
    path('api/', include(('api.urls', 'api'), namespace='rest_framework'))
]
