from django.shortcuts import render, get_object_or_404
from .models import Offer


def offers_view(request):
    offers = Offer.objects.all()
    available_offers = offers.filter(on_going=True)
    off_offers = offers.filter(on_going=False)
    template = "offers/offers.html"
    context = {
        'available_offers': available_offers,
        'off_offers': off_offers
    }
    return render(request, template, context)


def offer_details(request, offer_id):
    the_offer = get_object_or_404(Offer, pk=offer_id)
    template = 'offers/offer_details.html'
    context = {
        'offer': the_offer,
    }
    return render(request, template, context)
