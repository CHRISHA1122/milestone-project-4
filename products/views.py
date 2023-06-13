from django.shortcuts import render, get_object_or_404
from .models import Product, CustomizableProduct

# Create views


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)
    try:
        customizable_product = product.customizableproduct
    except CustomizableProduct.DoesNotExist:
        customizable_product = None

    context = {
        'product': product,
        'customizable_product': customizable_product,
    }

    return render(request, 'products/product_detail.html', context)
