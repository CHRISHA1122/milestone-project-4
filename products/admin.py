from django.contrib import admin
from .models import Category, Product, Color

# Register models


# Product admin model
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'rating',
        'image',
        'customizable'
    )

    list_editable = ('customizable',)

    fieldsets = (
        (None, {
            'fields': (
                'category', 'sku', 'name', 'description', 'price', 'image')
        }),
        ('Customization', {
            'fields': (
                'customizable', 'main_color', 'wording_color', 'writing'),
            'classes': ('collapse',)
        }),
    )


# Category admin model
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Color)
