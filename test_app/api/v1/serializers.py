from rest_framework import serializers
from test_app.models import TestingModel


class TestingModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestingModel
        fields = "__all__"
