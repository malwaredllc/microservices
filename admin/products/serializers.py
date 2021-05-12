from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializers):
    class Meta:
        model = Product
        fields = '__all__'
