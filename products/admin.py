from django.contrib import admin
from .models import Category, CustomizableProduct, Product, Color

# Register models


class CustomizableProductInline(admin.StackedInline):
    model = CustomizableProduct
    can_delete = False
    verbose_name_plural = 'Customizable Product'
    fk_name = 'product'
    fields = ['main_color', 'wording_color']


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
    inlines = (CustomizableProductInline,)

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if obj.customizable:
            if not hasattr(obj, 'customizableproduct'):
                CustomizableProduct.objects.create(product=obj)

        else:
            if hasattr(obj, 'customizableproduct'):
                obj.customizableproduct.delete()

    fieldsets = (
        (None, {
            'fields': ('category', 'sku', 'name', 'description', 'price', 'image')
        }),
        ('Customization', {
            'fields': ('customizable',),
        }),
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Color)
