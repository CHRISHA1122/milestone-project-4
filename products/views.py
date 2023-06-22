from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category, CustomizableProduct
from .forms import CustomizableProductForm
from .forms import ProductForm

# Create views


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
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


def add_product(request):
    """ Add a product to the store """
    form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


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
