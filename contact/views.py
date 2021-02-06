from django.shortcuts import render

# Create your views here.
def contact(request):
    template = "contact/contact.html"
    return render(request, template)