from django.contrib import admin
from .models import Category, CustomizableProduct, Product

# Register models


class CustomizableProductInline(admin.StackedInline):
    model = CustomizableProduct
    can_delete = False
    verbose_name_plural = 'Customizable Product'
    fk_name = 'product'


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
            obj.customizableproduct.delete()


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
