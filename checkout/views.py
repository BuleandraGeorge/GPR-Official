from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from .forms import OrderForm
from .models import Order, lineitem
from wines.models import wine
from decorators import security
from django.contrib import messages

@security
def checkout_success(request, order_number):
    order = Order.objects.get(order_number=order_number)
    email_send = request.session.get('email_send')
    if not email_send:
        cust_email = order.email
        lineitems = order.lineitem.all()
        subject = render_to_string('checkout/subject.txt', {"order": order})
        message = render_to_string('checkout/message.txt', 
            {"order": order,
            "items": lineitems,
            "contact_email": settings.DEFAULT_FROM_EMAIL,
            "contact_phone": settings.DEFAULT_PHONE})

        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [order.email,],)

        if 'bag' in request.session:
            del request.session['bag']
    context = {
        "order":order,
    }
    request.session['email_send'] = True
    template = "checkout/checkout_success.html"
    return render(request, template, context)

@security
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
        order = this_order.save()
        if this_order.is_valid:
            for item_id, item_data in bag.items():
                the_wine = get_object_or_404(wine, pk=item_id)
                for size, qty in item_data['size_qty'].items():
                    order_line_item = lineitem(
                        order=order,
                        the_wine=the_wine,
                        product_size=size,
                        quantity=qty,
                    )
                    order_line_item.save()
            request.session['email_send'] = False
            order.update_total()
        return redirect(reverse(
            'checkout_success',
            args=[order.order_number]))
    else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, "There's nothing in your bag at the moment")
            return redirect(reverse('wines_view'))
        template = "checkout/checkout.html"
        context = {
            "OrderForm": OrderForm,
        }
        return render(request, template, context)
