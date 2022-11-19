from rest_framework import viewsets

from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    The View Set for the Product model.

    Attributes:
        queryset (QuerySet): The queryset for all instances of the products to
            be used in our API.
        serializer_class (ProductSerializer): The serializer to be used to
            interact with the product model.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

