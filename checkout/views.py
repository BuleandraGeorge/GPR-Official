from django.shortcuts import render


def checkout_view(request):
    template = "checkout/checkout.html"
    return render(request, template)
