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

    def __str__(self):
        return self.name


# Customization Model
class CustomizableProduct(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category, null=True, blank=True, on_delete=models.SET_NULL)
    main_color = models.CharField(
        max_length=50, null=True, blank=True, choices=[])
    wording_color = models.CharField(
        max_length=50, null=True, blank=True, choices=[])
    writing = models.CharField(max_length=100, null=True, blank=True)

    def get_main_color_choices(self):

        if self.category and self.category.name == 'note_books':
            return [
                ('#FF0000', 'Red'),
                ('#0000FF', 'Blue'),
            ]

        elif self.category and self.category.name == 'toiletries':
            return [
                ('#000000', 'Black'),
                ('#FFFFFF', 'White'),
                ('#272727', 'Gray'),
            ]

        else:
            return [
                ('default_color', 'Default Color'),
            ]

    def get_wording_color_choices(self):

        if self.category and self.category.name == 'note_books':
            return [
                ('#000000', 'Black'),
                ('#FFFFFF', 'White',),
                ('#272727', 'Gray'),
            ]

        elif self.category and self.category.name == 'toiletries':
            return [
                ('#000000', 'Black'),
                ('#FFFFFF', 'White'),
                ('#272727', 'Gray'),
            ]

        else:
            return [
                ('default_color', 'Default Color'),
            ]

    def save(self, *args, **kwargs):
        self._meta.get_field(
            'main_color').choices = self.get_main_color_choices()
        self._meta.get_field(
            'wording_color').choices = self.get_wording_color_choices()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Customizable {self.product.name}"
