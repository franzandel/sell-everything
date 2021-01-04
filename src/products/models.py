from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    image_name = models.CharField(max_length=255, blank=False, null=False)
    seller = models.CharField(max_length=255, blank=False, null=False)
    quantity = models.CharField(max_length=255, blank=False, null=False)
    cashback = models.CharField(max_length=255, blank=False, null=False)
    discount_percentage = models.CharField(max_length=3, blank=False, null=False)
    price = models.CharField(max_length=255, blank=False, null=False)
    location = models.CharField(max_length=255, blank=False, null=False)
    weight = models.CharField(max_length=255, blank=False, null=False)
    condition = models.CharField(max_length=255, blank=False, null=False)
    min_order = models.CharField(max_length=255, blank=False, null=False)
    category = models.CharField(max_length=255, blank=False, null=False)
    description = models.CharField(max_length=2000, blank=False, null=False)

    def __str__(self) -> str:
        return self.title
