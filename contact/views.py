from django.shortcuts import render
from decorators import security


@security
def contact(request):
    template = "contact/contact.html"
    return render(request, template)