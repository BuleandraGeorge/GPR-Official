import uuid
from django.db.models import Sum
from django_countries.fields import CountryField
from django.db import models
from wines.models import wine


class Order(models.Model):
    order_number = models.CharField(max_length=255, null=False, blank=False)
    nume = models.CharField(max_length=50, null=False, blank=False)
    telefon = models.CharField(max_length=25, null=False, blank=False)
    email = models.EmailField(blank=False, null=False)
    adresa  = models.CharField(max_length=255, null=False, blank=False)
    adresa_linia_2 = models.CharField(max_length=255, null=True, blank=True)
    judet = models.CharField(max_length=50, null=False, blank=False)
    tara = CountryField(default='RO')
    date = models.DateField(auto_now=True)
    total = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    def _generate_order_number(self):
        return uuid.uuid4().hex.upper()

    def update_total(self):
        self.total = self.lineitem.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        self.save

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

class lineitem(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='lineitem')
    the_wine = models.ForeignKey(wine, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False, null=False)
    product_size = models.CharField(max_length=10, blank=False, null=False)
    lineitem_total = models.DecimalField(max_digits=8, decimal_places=2, blank=False, null=False)

    def save(self, *args, **kwargs):
        theSize = self.the_wine.size_details_set.filter(size__name=self.product_size)
        price = theSize[0].price
        self.lineitem_total = self.quantity * price
        super().save(*args, **kwargs)
