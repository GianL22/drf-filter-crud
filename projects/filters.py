from django_filters.rest_framework import FilterSet, RangeFilter, DateFromToRangeFilter
from .models import Product
class ProductFilter(FilterSet):
    price = RangeFilter()
    published_at = DateFromToRangeFilter()
    class Meta:
        model = Product
        fields = ['category', 'price', 'published_at']