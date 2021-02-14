from django.shortcuts import render
from django.db.models import Sum
from offers.models import Offer
from wines.models import wine, size_details

def home(request):
    offer = Offer.objects.all()
    displayed_offers = offer.filter(display=True)
    wines = wine.objects.all()
    size_detailss = size_details.objects.all()
    wines_qty_sold = wine.objects.annotate(
        total_sold=Sum('size_details__qty_sold'))
    best_sold = wines_qty_sold.order_by('-total_sold')[:4]
    best_rated = wines.order_by('-rating')[:4]
    new_arrivals = wines.order_by(
        '-first_time_listed__year',
        '-first_time_listed__month',
        '-first_time_listed__day')[:4]
    context = {
        'offers': displayed_offers,
        'best_sold': best_sold,
        'best_rated': best_rated,
        'new_arrivals': new_arrivals,
        'size_details':size_detailss,
    }
    template = "home/home.html"
    return render(request, template, context)
