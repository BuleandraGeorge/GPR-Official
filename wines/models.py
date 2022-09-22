from datetime import date
from django.db import models
from django.conf.global_settings import LANGUAGES
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

class size_details(models.Model):
    """ Informatii despre dimensiunea vinului """
    name = "Informatii despre dimensiunea vinului"
    wine = models.ForeignKey('wine', null=False, blank=False, on_delete=models.CASCADE)
    size = models.ForeignKey('size', null=False, blank=False, on_delete=models.PROTECT)
    qty_available = models.IntegerField(null=False, blank=False, default=0)
    qty_sold = models.IntegerField(null=False, blank=False, default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False)

    class Meta:
        verbose_name = "Dimensiune"
        verbose_name_plural = "Dimensiuni"

    def __str__(self):
        return self.name


class wine(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False, default="Fara nume")
    color = models.ForeignKey('color', null=False, blank=False, on_delete=models.PROTECT) 
    grape = models.ForeignKey('grape', null=False, blank=False, on_delete=models.PROTECT) 
    region = models.ForeignKey('region', null=False, blank=False, on_delete=models.PROTECT)  
    rating = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
    first_time_listed = models.DateField(default=date.today) 
    image_url = models.URLField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name

class translation(models.Model):
    language = models.CharField(max_length=7, choices=LANGUAGES )
    vinification = models.TextField(null=True, blank=True) 
    aging = models.TextField(null=True, blank=True)
    color_details = models.TextField(null=True, blank=True)
    palate = models.TextField(null=True, blank=True)
    serving = models.TextField(null=True, blank=True)
    boxing = models.TextField(null=True, blank=True)
    wine = models.ForeignKey('wine', null=True, on_delete=models.CASCADE)