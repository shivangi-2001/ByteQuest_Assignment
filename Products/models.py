from django.db import models

# Create your models here.
class Product(models.Model):
    COLLECTIONS_CHOICES = [
        ("ELECTRONIC", "Electronic"),
        ('Fashion', (
            ('WOMEN', 'Women'),
            ('MEN', 'Men'),
            )
        ),
        ("HOME APPLIANCES", 'Home Appliances'),
        ("VEHICLES", 'Vehicles')
    ]
    name = models.CharField(max_length=255)
    details = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2, null=False)
    collections = models.CharField(max_length=100, choices=COLLECTIONS_CHOICES, default='ELECTRONIC')