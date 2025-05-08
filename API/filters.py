import django_filters
from API.models import Product, Order
from rest_framework import filters


class InStockFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(stock__gt=6)

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        # fields = ["name","price"]

        fields ={
            'name':['iexact','icontains'],
            'price':['exact','lt','gt','range']
        }

class OrderFilter(django_filters.FilterSet):
    created_at = django_filters.DateFilter(field_name='created_at__date')
    class Meta:
        model = Order
        fields = {
            'status':['exact'],
            'created_at': ['lt', 'gt', 'exact']
        }