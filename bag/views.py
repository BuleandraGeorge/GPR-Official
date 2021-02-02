from django.shortcuts import render, redirect, reverse
from wines.models import wine


def bag_view(request):
    template="bag/bag.html"
    return render(request, template)

def add_to_bag(request, wine_id):
    size = request.POST['wine_size']
    quantity = int(request.POST['quantity'])
    bag = request.session.get('bag', {})
    redirect_url = request.POST['redirect_url']
    wine_id = str(wine_id)
    if wine_id in list(bag.keys()):
        if size in list(bag[wine_id]['size_qty'].keys()):
            bag[wine_id]['size_qty'][size] += quantity
        else:

            bag[wine_id]['size_qty'][size] = quantity
    else:
        bag[wine_id] = {'size_qty':{size: quantity}}
    request.session['bag'] = bag
    print(bag)
    return redirect(redirect_url)

def edit_bag(request, wine_id):
    qty = int(request.POST.get('quantity'))
    wine_id = str(wine_id)
    size = request.POST.get('size')
    bag = request.session.get('bag',{})
    if qty == 0:
        bag[wine_id]['size_qty'].pop(size)
    else:
        bag[wine_id]['size_qty'][size] = qty
    request.session['bag'] = bag
    return redirect(reverse('bag'))
