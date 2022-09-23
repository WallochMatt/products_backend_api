from rest_framework import serializers
from .models import Product

class ProductSerialiazers(serializers.Serializer):
    class Meta:
        model = Product
        fields = ['tilte', 'description', 'price', 'inventory_quantity']