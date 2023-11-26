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
    botanical_name = models.CharField(max_length=255, null=True, blank=True)
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL
    )
    description = models.TextField(null=True, blank=True)
    size = models.CharField(max_length=255, null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    discount_price = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True
    )
    rating = models.DecimalField(max_digits=5, decimal_places=2)
    preferred_light = models.CharField(
        max_length=20, choices=LIGHT_CHOICES,
        null=True, blank=True
    )
    watering_needs = models.CharField(
        max_length=10, choices=WATERING_CHOICES,
        null=True, blank=True
    )
    toxic = models.BooleanField(default=False)
    date = models.DateField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def calculate_sale_percentage(self):
        if self.discount_price is not None and self.price is not None and self.price > 0:
            # Calculate the sale percentage
            sale_percentage = (
                (self.price - self.discount_price) / self.price) * 100
            return round(sale_percentage, 2)
        else:
            return 0.0
