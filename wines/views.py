from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Min
from .models import wine, color, region, grape, size_details, size
from decorators import security
from django.utils.translation import get_language, get_language_info

@security
def wines_view(request):
    wines = wine.objects.all()
    size_detailss = size_details.objects.all()
    regions = region.objects.all()
    grapes = grape.objects.all()
    colors = color.objects.all()
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
    if "price" in request.GET:
        value = request.GET['price']
        wines = wines.annotate(lowest_price=Min('size_details__price'))
        if value == "price_desc":
            wines = wines.order_by("-lowest_price")
        else:
            wines = wines.order_by("lowest_price")
        categories.append(value)

    if "rating" in request.GET:
        value = request.GET['rating']
        if value == "rating_desc":
            wines = wines.order_by("-rating")
        else:
            wines = wines.order_by("rating")
        categories.append(value)
    if "q" in request.GET:
        query = request.GET['q']
        print(query)
        if query:
            current_language = get_language()[:2]
            wine_queries = Q(name__icontains=query) | Q(grape__name__icontains=query) | Q(region__name__icontains=query) | Q(color__name__icontains=query) 
            translation_queries = Q(translation__language=current_language) & (
                    Q(translation__vinification__icontains=query) | 
                    Q(translation__aging__icontains=query) | 
                    Q(translation__palate__icontains=query) | 
                    Q(translation__color_details__icontains=query)
            )
            wines = wine.objects.filter( wine_queries | translation_queries).distinct()
    context = {
        'wines': wines,
        'categories': categories,
        'regions': regions,
        'grapes': grapes,
        'size_details': size_detailss,
        'colors': colors
    }
    template = 'wines/wines.html'
    return render(request, template, context)



@security
def wine_details(request, wine_id):
    current_wine = get_object_or_404(wine, pk=wine_id)
    size_detailss = size_details.objects.all()
    current_language = get_language()[:2]
    translation = current_wine.translation_set.filter(language=current_language)
    if len(translation)>0:
        wine_details = translation[0]
    else:
        wine_details=current_wine.translation_set.all()[0]
    template = "wines/wine_details.html"
    context = {
        "wine": current_wine,
        "wine_details":wine_details,
        "wine_sizes": size_detailss,
    }
    return render(request, template, context)