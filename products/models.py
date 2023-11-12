from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    LIGHT_CHOICES = [
        ('Indirect Light', 'Indirect Light'),
        ('Bright Light', 'Bright Light'),
        ('Low Light', 'Low Light'),
    ]

    WATERING_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]
    sku = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255)
    botanical_name = models.CharField(max_length=255)
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL
    )
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)
    size = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    discount_price = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True
    )
    rating = models.DecimalField(max_digits=5, decimal_places=2)
    preferred_light = models.CharField(
        max_length=20, choices=LIGHT_CHOICES, default='Indirect Light'
    )
    watering_needs = models.CharField(
        max_length=10, choices=WATERING_CHOICES, default='Medium'
    )
    toxic = models.BooleanField(default=False)
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name
