from django.db import models
from colorfield.fields import ColorField


class Offer(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    hook = models.CharField(max_length=255, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)
    text_color = ColorField(default='#000000')
    display = models.BooleanField(default=False)
    on_going = models.BooleanField(default=True)

    def __str__(self):
        return self.title