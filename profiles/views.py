from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from checkout.models import Order
from .models import UserProfile
from .forms import UserProfileForm


@login_required
def profile_view(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid:
            form.save()
            messages.success(request, 'Profilul a fost actualizat!')
        else:
            messages.error(request, 'Ceva nu a mers bine, verificati formularul si incercati inca o data.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()
    context = {
        'form': form,
        'orders': orders
    }
    template = 'profiles/profiles.html'
    return render(request, template,  context)


def order_history(request, order_number):
    curr_order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'Aceasta este doar o confirmare a comenzii {order_number}. '
        'Un email de confirmare a fost trimis la data comenzii'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': curr_order,
        'from_profile': True,
    }

    return render(request, template, context)