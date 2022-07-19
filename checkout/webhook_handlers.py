from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .models import Order, lineitem
from wines.models import wine
from profiles.models import UserProfile

import json
import time

class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """Send the user a confirmation email"""
        cust_email = order.email
        lineitems = order.lineitem.all()
        subject = render_to_string('checkout/subject.txt', {"order": order})
        message = render_to_string('checkout/message.txt', 
            {"order": order,
            "items": lineitems,
            "contact_email": settings.DEFAULT_FROM_EMAIL,
            "contact_phone": settings.DEFAULT_PHONE})

        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [order.email,],)        

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        # Clean data in the shipping details
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        # Update profile information if save_info was checked
        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            profile = UserProfile.objects.get(user__username=username)
            if save_info:
                profile.default_phone_number = shipping_details.phone
                profile.default_country = shipping_details.address.country
                profile.default_town_or_city = shipping_details.address.city
                profile.default_street_address1 = shipping_details.address.line1
                profile.default_street_address2 = shipping_details.address.line2
                profile.save()

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    nume__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    telefon__iexact=shipping_details.phone,
                    tara__iexact=shipping_details.address.country,
                    judet__iexact=shipping_details.address.city,
                    adresa__iexact=shipping_details.address.line1,
                    adresa_linia_2__iexact=shipping_details.address.line2,
                    total=grand_total,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            self._send_confirmation_email(order)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    nume=shipping_details.name,
                    user_profile=profile,
                    email=billing_details.email,
                    telefon=shipping_details.phone,
                    tara=shipping_details.address.country,
                    judet=shipping_details.address.city,
                    adresa=shipping_details.address.line1,
                    adresa_linia_2=shipping_details.address.line2,
                    original_bag=bag,
                    stripe_pid=pid,
                )
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
                order.update_total()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        self._send_confirmation_email(order)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
