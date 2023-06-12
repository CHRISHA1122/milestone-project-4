from django.db import models

# Create models


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
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    # Customization fields
    customizable = models.BooleanField(default=False)
    main_color = models.CharField(
        max_length=50, null=True, blank=True, choices=[])
    wording_color = models.CharField(
        max_length=50, null=True, blank=True, choices=[])
    writing = models.CharField(max_length=100, null=True, blank=True)

    def get_main_color_choices(self):

        if self.category.name == 'note_books':
            return [
                ('red', 'Red'),
                ('blue', 'Blue'),
            ]

        elif self.category.name == 'toiletries':
            return [
                ('black', 'Black'),
                ('white', 'White'),
                ('gray', 'Gray'),
            ]

        else:
            return [
                ('default_color', 'Default Color'),
            ]

    def get_wording_color_choices(self):

        if self.category.name == 'note_books':
            return [
                ('black', 'Black'),
                ('white', 'White',),
                ('gray', 'Gray'),
            ]

        elif self.category.name == 'toiletries':
            return [
                ('black', 'Black'),
                ('white', 'White'),
                ('gray', 'Gray'),
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
        return self.name
