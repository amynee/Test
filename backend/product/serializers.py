from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'PRDName', 'PRDBrand', 'PRDDesc', 'PRDPrice', 'PRDCost','PRDDiscount','PRDInstock','PRDIImage', 'PRDCreated']

