from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages
from products.models import Product

# Create views


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = request.POST.get('product_size')
    main_color = request.POST.get('main_color')
    wording_color = request.POST.get('wording_color')
    writing = request.POST.get('writing')
    bag = request.session.get('bag', {})

    if 'product_size' in request.POST:
        size = request.POST['product_size']

    if product.customizable:
        main_color = request.POST.get('main_color')
        wording_color = request.POST.get('wording_color')
        writing = request.POST.get('writing')

    if item_id in bag:
        if 'items_by_size' in bag[item_id]:
            items_by_size = bag[item_id]['items_by_size']
            if isinstance(items_by_size, int):
                bag[item_id]['items_by_size'] = {size: quantity}
                messages.success(request, f'Added size {size.upper() if size else "N/A"} {product.name} to your bag')
            elif isinstance(items_by_size, dict) and size in items_by_size:
                bag[item_id]['items_by_size'][size] += quantity
                messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {bag[item_id]["items_by_size"][size]}')
            else:
                bag[item_id]['items_by_size'][size] = quantity
                messages.success(request, f'Added size {size.upper()} {product.name} to your bag')
        else:
            if size:
                bag[item_id]['items_by_size'] = {size: quantity}
                messages.success(request, f'Added size {size.upper()} {product.name} to your bag')
            else:
                bag[item_id]['items_by_size'] = quantity
                messages.success(request, f'Added {product.name} to your bag')
    else:
        if product.customizable:
            bag[item_id] = {'items_by_size': {size: quantity}}
            bag[item_id]['main_color'] = main_color
            bag[item_id]['wording_color'] = wording_color
            bag[item_id]['writing'] = writing
            messages.success(request, f'Added {product.name} to your bag')
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
            messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    main_color = None
    wording_color = None
    writing = None
    bag = request.session.get('bag', {})

    if 'product_size' in request.POST:
        size = request.POST['product_size']
    print(f"Size: {size}")

    if product.customizable:
        main_color = request.POST.get('main_color')
        wording_color = request.POST.get('wording_color')
        writing = request.POST.get('writing')

    if size:
        if item_id in bag and 'items_by_size' in bag[item_id] and size in bag[item_id]['items_by_size']:
            bag[item_id]['items_by_size'][size] = quantity
            messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {bag[item_id]["items_by_size"][size]}')
        else:
            messages.error(request, 'Item size does not exist in your bag')
    else:
        if item_id in bag and isinstance(bag[item_id], int):
            bag[item_id] = {
                'quantity': bag[item_id],
                'main_color': main_color,
                'wording_color': wording_color,
                'writing': writing
            }
        elif item_id in bag:
            bag[item_id]['main_color'] = main_color
            bag[item_id]['wording_color'] = wording_color
            bag[item_id]['writing'] = writing
            bag[item_id]['quantity'] = quantity
        else:
            bag[item_id] = {
                'main_color': main_color,
                'wording_color': wording_color,
                'writing': writing,
                'quantity': quantity
            }

        messages.success(request, f'Updated {product.name} quantity to {bag[item_id]["quantity"]}')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        bag = request.session.get('bag', {})
        product = get_object_or_404(Product, pk=item_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']

        if size:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(request, f'Removed size {size.upper()} {product.name} from your bag')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
