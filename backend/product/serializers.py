from rest_framework import serializers

from .models import Product, ProductImage

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        field = fields = ['PRDName', 'PRDBrand', 'PRDDesc', 'PRDPrice', 'PRDCost', 'PRDCreated']

class ProductImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductImage
        field = fields = ['PRDIproduct', 'PRDIImage']