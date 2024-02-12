from rest_framework import serializers
from .models import Project, Product

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'technology', 'created_at')
        read_only_fields = ('created_at',)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'description', 'category', 'price', 'discount', 'color', 'size', 'published_at')
        read_only_fields = ('published_at',)