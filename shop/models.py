from django.db import models

# Create your models here.


class ShopProducts(models.Model):

    class Meta:
        verbose_name_plural = 'ShopProducts'

    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=250)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name