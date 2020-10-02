from django.db import models

# Create your models here.


class Order(models.Model):
    """
    docstring
    """
    token = models.CharField(max_length=250, blank=True)
    total = models.DecimalField(
        verbose_name="GBP Order Total", max_digits=10, decimal_places=2)
    emailAddress = models.EmailField(
        verbose_name="Email Address", max_length=254, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    billingName = models.CharField(max_length=250, blank=True)
    billingAddress1 = models.CharField(max_length=250, blank=True)
    billingCity = models.CharField(max_length=250, blank=True)
    billingPostCode = models.CharField(max_length=250, blank=True)
    billingCountry = models.CharField(max_length=250, blank=True)
    shippingName = models.CharField(max_length=250, blank=True)
    shippingAddress1 = models.CharField(max_length=250, blank=True)
    shippingCity = models.CharField(max_length=250, blank=True)
    shippingPostCode = models.CharField(max_length=250, blank=True)
    shippingCountry = models.CharField(max_length=250, blank=True)

    class Meta:
        """
        docstring
        """
        db_table = 'Order'
        ordering = ['-created']

    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    """
    docstring
    """
    product = models.CharField(max_length=254)
    quantity = models.IntegerField()
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="GBP Order Total",)
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE)

    class Meta:
        """
        docstring
        """
        db_table = 'OrderItem'

    def sub_total(self):
        return self.quantity * self.price

    def __str__(self):
        return self.product
