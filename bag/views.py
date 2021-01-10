from django.shortcuts import render


def bag_view(request):
    template="bag/bag.html"
    return render(request,template)
