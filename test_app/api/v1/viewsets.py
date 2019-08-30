from rest_framework.viewsets import ModelViewSet
from test_app.models import TestingModel
from .serializers import TestingModelSerializer


class TestingModelViewSet(ModelViewSet):
    serializer_class = TestingModelSerializer
    queryset = TestingModel.objects.all()
