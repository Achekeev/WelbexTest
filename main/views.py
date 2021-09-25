from rest_framework import generics
from .models import TestTable
from .serializers import TestTableSerializer
from django_filters import rest_framework as filters


class TestTableFilter(filters.FilterSet):
    date_range = filters.DateRangeFilter(field_name="date")
    amount_range = filters.RangeFilter(field_name="amount")
    distance_range = filters.RangeFilter(field_name="distance")
    name_filter = filters.AllValuesFilter(field_name="name")


class TestTableAPIView(generics.ListCreateAPIView):
    queryset = TestTable.objects.all()
    serializer_class = TestTableSerializer
    filter_class = TestTableFilter
    filterset_fields = ("date", "name", "amount", "distance")
