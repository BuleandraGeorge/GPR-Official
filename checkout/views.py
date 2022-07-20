import os
from django.shortcuts import render, get_object_or_404, reverse, redirect, HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.views.decorators.http import require_POST
from django.contrib import messages
from .forms import OrderForm
from .models import Order, lineitem
from profiles.models import UserProfile
from wines.models import wine
from decorators import security

from bag.contexts import bag_content

### STRIPE ####

import stripe
import json
 
@security
def checkout_success(request, order_number):
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()

        # Save the user's info
        if save_info:
            profile_data = {
                'default_name': order.nume,
                'default_phone_number': order.telefon,
                'default_country': order.tara,
                'default_town_or_city': order.judet,
                'default_street_address1': order.adresa,
                'default_street_address2': order.adresa_linia_2,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(request, f'Comanda a fost procesata cu success! \
        Numarul comenzii este {order_number}. Un email de confirmare va fi trimis \
        la {order.email}.')

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
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
       
        if this_order.is_valid:
            order = this_order.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            order.save()
            for item_id, item_data in bag.items():
                try:
                    the_wine = get_object_or_404(wine, pk=item_id)
                    for size, qty in item_data['size_qty'].items():
                        order_line_item = lineitem(
                            order=order,
                            the_wine=the_wine,
                            product_size=size,
                            quantity=qty,
                        )
                        order_line_item.save()
                except wine.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your bag wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('bag'))

            order.update_total()
            return redirect(reverse('checkout_success',args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        if not bag:
            messages.error(request, "There's nothing in your bag at the moment")
            return redirect(reverse('wines_view'))
        current_bag = bag_content(request)
        total = current_bag['total']
        stripe_total = round(total*100)
        stripe.api_key = settings.STRIPE_SK
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency='RON',
        )
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                     "nume":profile.default_name,
                     "telefon":profile.default_phone_number,
                     "email": profile.user.email,
                     "adresa":profile.default_street_address1,
                     "adresa_linia_2": profile.default_street_address2,
                     "judet":profile.default_town_or_city,
                     "tara":profile.default_country,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

        template = "checkout/checkout.html"
        context = {
            "OrderForm": order_form,
            "stripe_public_key": settings.STRIPE_PK,
            "client_secret": intent.client_secret
        }
        return render(request, template, context)
@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SK
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Ne pare rau dar plata \
            nu se poate face momentan. Va rugam incercati mai tarziu.')
        return HttpResponse(content=e, status=400)