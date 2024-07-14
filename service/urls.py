from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
# Create a router and register our viewsets with it.

router = DefaultRouter()

router.register('', views.ServiceViewset)
urlpatterns = [
    path('', include(router.urls)),
]
