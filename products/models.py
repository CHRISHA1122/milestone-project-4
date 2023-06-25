from django.db import models
from django.forms import inlineformset_factory

# Create models


# Category Model
class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


# Color Model
class Color(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# Product Model
class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    customizable = models.BooleanField(default=False)
    colors = models.ManyToManyField(Color)

    def __str__(self):
        return self.name


# Customization Model
class CustomizableProduct(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category, null=True, blank=True, on_delete=models.SET_NULL)
    main_color = models.ForeignKey(
        Color, related_name='main_color_products', null=True, blank=True, on_delete=models.SET_NULL)
    wording_color = models.ForeignKey(
        Color, related_name='wording_color_products', null=True, blank=True, on_delete=models.SET_NULL)
    writing = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"Customizable {self.product.name}"
