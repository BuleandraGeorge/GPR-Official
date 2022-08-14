from django import forms
from .models import Order
from django.utils.translation import gettext_lazy as _
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
        labels = {
            'nume': _("Nume"),
            'telefon':_('Telefon'),
            'adresa':_('Adresa'),
            'adresa_linia_2':_('Adresa linia 2'),
            'judet':_('Judet'),
            'tara':_('Tara')
        }
