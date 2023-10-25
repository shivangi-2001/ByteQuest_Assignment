from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'details', 'price', 'collections','tax_on_product']

    tax_on_product = serializers.SerializerMethodField(
        method_name='auto_tax'
    )
    def auto_tax(self, product: Product):
        if product.collections == 'ELECTRONIC':
            return round(float(product.price) * 1.80, 2)
        elif product.collections == 'MEN':
            return round(float(product.price) * 1.52, 2)
        elif product.collections == 'WOMEN':
            return round(float(product.price) * 2.90, 2)
        elif product.collections == 'HOME APPLIANCES':
            return round(float(product.price) * 1.1, 2)
        elif product.collections == 'VEHICLES':
            return round(float(product.price) * 10.79, 2)

