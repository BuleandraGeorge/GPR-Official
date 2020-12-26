from django.shortcuts import render


def wines_view(request):
    template = 'wines/wines.html'
    return render(request, template)
