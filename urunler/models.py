# urunler/models.py

from django.db import models

class Product(models.Model):
    UNIT_CHOICES = [
        ('adet', 'Adet'),
        ('kilo', 'Kilo'),
        ('koli', 'Koli'),
        ('adet-koli', 'Adet + Koli'),
    ]

    barcode = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=255)
    unit_type = models.CharField(max_length=20, choices=UNIT_CHOICES)
    unit_per_package = models.PositiveIntegerField(null=True, blank=True)
    stock_quantity = models.FloatField(default=0)

    def __str__(self):
        return f"{self.name} ({self.barcode})"
