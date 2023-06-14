from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, CustomizableProduct
from .forms import CustomizableProductForm

# Create views


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
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


def customize_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    try:
        customizable_product = product.customizableproduct
    except CustomizableProduct.DoesNotExist:
        customizable_product = None

    if request.method == 'POST':
        form = CustomizableProductForm(
            request.POST, instance=customizable_product)
        if form.is_valid():
            form.save()

    else:
        form = CustomizableProductForm(instance=customizable_product)

    context = {
        'product': product,
        'customizable_product': customizable_product,
        'form': form,
    }

    return render(request, 'products/product_detail.html', context)
