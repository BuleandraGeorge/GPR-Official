from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta():
        model = Order
        fields = ('nume',
                    'telefon',
                    'email',
                    'adresa',
                    'adresa_linia_2',
                    'judet',
                    'tara',)

