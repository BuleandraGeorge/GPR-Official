from django.shortcuts import render
from django.db.models import Sum
from offers.models import Offer
from wines.models import wine, size_quantity_sold


def home(request):
    offer = Offer.objects.all()
    wines = wine.objects.all()
    displayed_offers = offer.filter(display=True)
    wines = wine.objects.all().annotate(total=Sum('size_quantity_sold'))
    wines_sizes = []
    i=0
    for product in wines:
        product_sizes = product.size_quantity_available_set.all()
        product_quantity_sold = product.size_quantity_sold_set.all()
        wines_sizes.append({
            'wine':product.id,
            'size_quantities':[]
        })
        for dim in product_sizes:
            wines_sizes[i]['size_quantities'].append(
                {
                    'size': dim.size,
                    'quantity_available': dim.quantity,
                    'quantity_sold:':0
                })
        # goes through every size of the product with quantity sold and updates the quantity sold in the template array
        for index, sold in enumerate(product_quantity_sold):
            wines_sizes[i]['size_quantities'][index]['quantity_sold'] = sold.quantity
        i+=1

    best_sold = wines.order_by('-total')[:4]
    best_rated = wines.order_by('-rating')[:4]
    new_arrivals = wines.order_by('first_time_listed')[:4]
    context = {
        'offers': displayed_offers,
        'best_sold': best_sold,
        'best_rated': best_rated,
        'new_arrivals': new_arrivals,
        'wines_sizes': wines_sizes
    }
    template = "home/home.html"
    return render(request, template, context)
