from django.db import models

class color(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return self.name


class grape(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return self.name


class region(models.Model):
    name = models.CharField(max_length=256,null=True, blank=True)

    def __str__(self):
        return self.name

class size(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return self.name

class size_quantity_available(models.Model):
    """ Model for storing quantity available per size wine """
    name = "Introduceti cantitatea disponibila pentru dimensiunea selectata"
    wine = models.ForeignKey('wine', null=False, blank=False, on_delete=models.CASCADE)
    size = models.ForeignKey('size', null=False, blank=False, on_delete=models.PROTECT)
    quantity = models.IntegerField(null=False, blank=False, default=0)

    class Meta:
        verbose_name = "Cantitate disponibila per dimensiune dimensiune"
        verbose_name_plural = "Cantitate disponibila per dimensiune dimensiune"

    def __str__(self):
        return self.name


class size_quantity_sold(models.Model):
    """ Model for storing quantity sold per size wine """
    name = "Cantitate vanduta per dimensiune"
    wine = models.ForeignKey('wine', null=False, blank=False, on_delete=models.CASCADE)
    size = models.ForeignKey('size', null=False, blank=False, on_delete=models.PROTECT)
    quantity = models.IntegerField(null=False, blank=False, default=0)

    class Meta:
        verbose_name = "Cantitate vanduta per dimensiune dimensiune"
        verbose_name_plural = "Cantitate vanduta per dimensiune dimensiune"

    def __str__(self):
        return self.name


class wine(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False, default="Fara nume")
    color = models.ForeignKey('color', null=False, blank=False, on_delete=models.PROTECT)  # main color category red, white, rose
    grape = models.ForeignKey('grape', null=False, blank=False, on_delete=models.PROTECT)  # the grapes the wine was made of 
    region = models.ForeignKey('region', null=False, blank=False, on_delete=models.PROTECT)  # the region where the wine comes from
    vinification = models.TextField(null=True, blank=True) 
    aging = models.TextField(null=True, blank=True)
    color_details = models.TextField(null=True, blank=True)
    palate = models.TextField(null=True, blank=True)
    serving = models.TextField(null=True, blank=True)
    boxing = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False)
    rating = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
    first_time_listed = models.DateField(auto_now=True) 
    image_url = models.URLField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    only_for_admin = models.BooleanField(default=True)  # to hide/unhide a product for customers if you want to do some test like image text etc...

    def __str__(self):
        return self.name