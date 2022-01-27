from django.db import models

# Create your models here.


class ShopProducts(models.Model):

    class Meta:
        verbose_name_plural = 'ShopProducts'

    sku = models.CharField(max_length=254, null=True, blank=False)
    category = models.CharField(max_length=7, null=True, blank=False)
    name = models.CharField(max_length=250, null=True, blank=False)
    description = models.TextField(null=True, blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=False)
    image = models.ImageField(null=True, blank=False)

    def __str__(self):
        return self.name