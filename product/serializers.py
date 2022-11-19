from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    status_name = serializers.ReadOnlyField()
    discount = serializers.ReadOnlyField()
    final_price = serializers.ReadOnlyField()

    class Meta:
        model = Product
        fields = (
            'product_id',
            'name',
            'status_name',
            'stock',
            'description',
            'price',
            'discount',
            'final_price'
        )