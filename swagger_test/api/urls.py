
from django.urls import path
from .views import TestView


urlpatterns = [
    # path('users/', UserViewSet.as_view({'get': 'list'})),
    path('test/', TestView.as_view()),
    path('test/<str:id>', TestView.as_view()),
    path('image/<str:id>', TestView.as_view())
]
