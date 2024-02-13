from django.shortcuts import render
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product
from .serializers import ProductSerializer
from .filters import ProductFilter
# Create your views here.


class ProductView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [
        IsAuthenticated
    ]
    filter_backends = [DjangoFilterBackend, SearchFilter, ]
    filterset_class = ProductFilter
    search_fields = ['title', 'description']

class RetrieveUpdateDestroyProductView(RetrieveUpdateDestroyAPIView):
    pass