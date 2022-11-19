from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    """
    The model serializer for the products.

    Attributes:
        status_name (serializers.ReadOnlyField()): A read only field which
            calls the property status_name from the model.
        discount (serializers.ReadOnlyField()): A read only field which calls
            the property discount from the model.
        final_price (serializers.ReadOnlyField()): A read only field which
            calls the property final_price from the model.
    """
    status_name = serializers.ReadOnlyField()
    discount = serializers.ReadOnlyField()
    final_price = serializers.ReadOnlyField()

    class Meta:
        """
        This sub-class is used to declare the model which this serializer will
        use, and the fields with which the user can interact.

        Attributes:
            model (Product): The Django ORM model for the products.
            fields (Tuple(str)): The fields with which the user can interact.
        """
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