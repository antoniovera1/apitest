from django.db import models

from services.random_org import get_random_int


class Product(models.Model):
    """
    This is the models class for the products on the Django ORM.

    Attributes:
        product_id (models.AutoField): The ID of the product. This is the
            primary key.
        name (models.CharField): The name of the product.
        status (models.IntegerField): The status of the product. This tells us
            if the product is active.
        stock (models.IntegerField): The number of products on stock.
        description (models.TextField): The description of the product.
        price (models.DecimalField): The price of the product.

    """

    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    status = models.IntegerField(default=1, choices=((1, "Active"), (0, 'Inactive')))
    stock = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=252, decimal_places=2)
    part_number = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)

    @property
    def discount(self):
        """
        Finds the discount on the product by using an external API to generate
        a random integer between 0 and 100.

        Returns:
            int: A random integer.
        """
        return get_random_int()

    @property
    def final_price(self):
        """
        Calculates the final price of the product by substracting the discount.

        Returns:
            float: The final price of the product.
        """
        return float(self.price) * ((100-self.discount) / 100)
