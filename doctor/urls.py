from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
# Create a router and register our viewsets with it.

router = DefaultRouter()

router.register('list', views.DoctorViewset)
router.register('specialization', views.SpecializationViewset)
router.register('designation', views.DesignationViewset)
router.register('available_time', views.AvailableTimeViewset)
router.register('reviews', views.ReviewViewset)
urlpatterns = [
    path('', include(router.urls)),
]
