from rest_framework import serializers
from .models import TestTable


class TestTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestTable
        fields = ("date", "name", "amount", "distance")
