from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import TestingModelViewSet

router = DefaultRouter()
router.register("testingmodel", TestingModelViewSet)

urlpatterns = [path("", include(router.urls))]
