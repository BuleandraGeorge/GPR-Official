from django.shortcuts import render, get_object_or_404
from .models import wine, color, region, grape, size_details, size


def wines_view(request):
    wines = wine.objects.all()
    size_detailss = size_details.objects.all()
    regions = region.objects.all()
    grapes = grape.objects.all()
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
    ### Ordered by price, needs updates acc new wine model
    """if "price" in request.GET:
        value = request.GET['price']
        if value == "price_desc":
            wines = wines.order_by("-price")
        else:
            wines = wines.order_by("price")
        categories.append(value)"""

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
        'size_details': size_detailss,
    }
    template = 'wines/wines.html'
    return render(request, template, context)

def wine_details(request, wine_id):
    current_wine = get_object_or_404(wine, pk=wine_id)
    size_detailss = size_details.objects.all()

    template = "wines/wine_details.html"
    context = {
        "wine": current_wine,
        "wine_sizes": size_detailss,
    }
    return render(request, template, context)