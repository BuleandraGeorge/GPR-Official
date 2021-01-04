from django.shortcuts import render
from .models import wine, color, region, grape, size_quantity_available, size_quantity_sold, size


def wines_view(request):
    wines = wine.objects.all()
    regions = region.objects.all()
    grapes = grape.objects.all()
    # template array which stores every product with sizes and quantities available or sold
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
    categories = []
    if "color" in request.GET:
        value = request.GET['color']
        wines = wines.filter(color__name=value)
        categories.append(value)

    if "region" in request.GET:
        value = request.GET['region']
        wines = wines.filter(region__name=value)
        categories.append(value)

    if "grape" in request.GET:
        value = request.GET['grape']
        wines = wines.filter(grape__name=value)
        categories.append(value)

    if "price" in request.GET:
        value = request.GET['price']
        if value == "price_desc":
            wines = wines.order_by("-price")
        else:
            wines = wines.order_by("price")
        categories.append(value)

    if "rating" in request.GET:
        value = request.GET['rating']
        if value == "rating_desc":
            wines = wines.order_by("-rating")
        else:
            wines = wines.order_by("rating")
        categories.append(value)
    context = {
        'wines': wines,
        'categories': categories,
        'regions': regions,
        'grapes': grapes,
        'wines_sizes': wines_sizes,
    }
    template = 'wines/wines.html'
    return render(request, template, context)
