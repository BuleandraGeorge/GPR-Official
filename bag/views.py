from django.shortcuts import render, redirect, reverse, get_object_or_404
from wines.models import wine
from decorators import security
from django.contrib import messages

@security
def bag_view(request):
    template="bag/bag.html"
    return render(request, template)


@security
def add_to_bag(request, wine_id):
    size = request.POST['wine_size']
    quantity = int(request.POST['quantity'])
    bag = request.session.get('bag', {})
    redirect_url = request.POST['redirect_url']
    curr_wine = get_object_or_404(wine, pk=wine_id)
    wine_id = str(wine_id)
    if wine_id in list(bag.keys()):
        if size in list(bag[wine_id]['size_qty'].keys()):
            bag[wine_id]['size_qty'][size] += quantity
        else:
            bag[wine_id]['size_qty'][size] = quantity
    else:
        bag[wine_id] = {'size_qty':{size: quantity}}
    request.session['bag'] = bag
    
    messages.success(request, f'{quantity} x {curr_wine.name} {size} au fost adaugate in cos')
    return redirect(redirect_url)


@security
def edit_bag(request, wine_id):
    qty = int(request.POST.get('quantity'))
    curr_wine = get_object_or_404(wine, pk=wine_id)
    wine_id = str(wine_id)
    size = request.POST.get('size')
    bag = request.session.get('bag',{})
    if qty < 1:
        bag[wine_id]['size_qty'].pop(size)
        if not bag[wine_id]['size_qty']:
            bag.pop(wine_id)
    else:
        bag[wine_id]['size_qty'][size] = qty
    messages.success(request, f'Cantitatea pentru {curr_wine.name} {size} a fost modificata la {qty}')
    request.session['bag'] = bag
    return redirect(reverse('bag'))
