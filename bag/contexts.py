from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product, Color


def bag_contents(request):
    # Handles bag contents

    bag_items = []
    total = 0
    product_count = 0
    delivery = 0
    bag = request.session.get('bag', {})
    if isinstance(bag, int):
        bag = {}

    for item_id, item_data in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        size = request.POST.get('product_size')
        main_color = request.POST.get('main_color')
        wording_color = request.POST.get('wording_color')
        writing = request.POST.get('writing')

        items_by_size = item_data.get('items_by_size')

        # Handle products with sizes
        if 'items_by_size' in item_data and isinstance(items_by_size, dict):
            for size, quantity in item_data['items_by_size'].items():
                if product.customizable:
                    main_color_id = item_data.get('main_color')
                    wording_color_id = item_data.get('wording_color')
                    writing = item_data.get('writing')

                    main_color = get_object_or_404(
                        Color, pk=main_color_id) if main_color_id else None
                    wording_color = get_object_or_404(
                        Color, pk=wording_color_id) if wording_color_id else None

                    bag_items.append({
                        'item_id': item_id,
                        'size': size,
                        'quantity': quantity,
                        'product': product,
                        'main_color': main_color,
                        'wording_color': wording_color,
                        'writing': writing,
                    })

                    total += quantity * product.price
                    product_count += quantity
                else:
                    bag_items.append({
                        'item_id': item_id,
                        'size': size,
                        'quantity': quantity,
                        'product': product,
                    })

                    total += quantity * product.price
                    product_count += quantity
        else:  # Handle products without sizes
            quantity = item_data.get('quantity', 0)

            if product.customizable:
                main_color_id = item_data.get('main_color')
                wording_color_id = item_data.get('wording_color')
                writing = item_data.get('writing')

                main_color = get_object_or_404(
                    Color, pk=main_color_id) if main_color_id else None
                wording_color = get_object_or_404(
                    Color, pk=wording_color_id) if wording_color_id else None

                bag_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'main_color': main_color,
                    'wording_color': wording_color,
                    'writing': writing,
                })

                total += quantity * product.price
                product_count += quantity
            else:
                bag_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                })

                total += quantity * product.price
                product_count += quantity

    delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context
