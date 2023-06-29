from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product, Color


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    delivery = 0
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        product = get_object_or_404(Product, pk=item_id)

        if isinstance(item_data, int):
            quantity = item_data
            main_color = None
            wording_color = None
            writing = None
        else:
            quantity = item_data['quantity']
            main_color = item_data.get('main_color')
            wording_color = item_data.get('wording_color')
            writing = item_data.get('writing')

        total += quantity * product.price
        product_count += quantity

        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
            'main_color': main_color,
            'wording_color': wording_color,
            'writing': writing,
        })

        print(f"Item ID: {item_id}")
        print(f"Main Color: {main_color}")
        print(f"Wording Color: {wording_color}")
        print(f"Writing: {writing}")

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
