from django.contrib import admin
from .models import Product, Category

# Register models
admin.site.register(Product)
admin.site.register(Category)
