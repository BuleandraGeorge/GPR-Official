from django.shortcuts import get_object_or_404
from wines.models import wine, color
from decimal import Decimal

def bag_content(request):
    bag = request.session.get('bag', {})
    bag_items = []
    total = 0
    for item_id, size_qty in bag.items():
        winee = get_object_or_404(wine, pk=item_id)
        for size, quantity in size_qty['size_qty'].items():
            theSize = winee.size_details_set.filter(size__name=size)
            price = theSize[0].price
            bag_items.append({
                "wine": winee,
                "size": size,
                "qty": quantity,
                "price": price,
            })
            total = total + Decimal(quantity) * price
    colors = color.objects.all()
    context = {
        "bag_items": bag_items,
        "total": total,
        "colors":colors
    }

    return context
