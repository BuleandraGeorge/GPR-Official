from django.shortcuts import render, get_object_or_404, reverse, redirect
from .forms import OrderForm
from .models import Order, lineitem
from wines.models import wine

def checkout_success(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)
    if 'bag' in request.session:
        del request.session['bag']
    context = {
        "order":order,
    }
    template = "checkout/checkout_success.html"
    return render(request, template, context)


def checkout_view(request):
    bag = request.session.get('bag', {})
    if request.method == "POST":
        order_details = {
            'nume': request.POST['nume'],
            'telefon': request.POST['telefon'],
            'email': request.POST['email'],
            'adresa': request.POST['adresa'],
            'adresa_linia_2': request.POST['adresa_linia_2'],
            'judet': request.POST['judet'],
            'tara': request.POST['tara']
        }
        this_order = OrderForm(order_details)
        if this_order.is_valid:
            order = this_order.save()
            for item_id, item_data in bag.items():
                the_wine = get_object_or_404(wine, pk=item_id)
                for size, qty in item_data['size_qty'].items():
                    print(size)
                    print(qty)
                    order_line_item = lineitem(
                        order=order,
                        the_wine=the_wine,
                        product_size=size,
                        quantity=qty,
                    )
                    order_line_item.save()
        return redirect(reverse(
            'checkout_success',
            args=[order.order_number]))
    else:
        template = "checkout/checkout.html"
        context = {
            "OrderForm": OrderForm,
        }
        return render(request, template, context)
