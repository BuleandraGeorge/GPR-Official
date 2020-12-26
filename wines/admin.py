from django.contrib import admin

from .models import wine, color, grape, region, size, size_quantity_available,size_quantity_sold


class wineQuantityAvailableDetailsAdmin(admin.TabularInline):
    model = size_quantity_available


class wineQuantitySoldDetailsAdmin(admin.TabularInline):
    model = size_quantity_sold
    readonly_fields = ('size', 'quantity')

class wineAdmin(admin.ModelAdmin):
    inlines = (wineQuantityAvailableDetailsAdmin, wineQuantitySoldDetailsAdmin,)
    list_display = (
        'name',
        'color',
        'region',
        'grape',
        'first_time_listed',
        'price',
        'rating',
        'image',
    )
    ordering = ('first_time_listed',)


admin.site.register(wine, wineAdmin)
admin.site.register(grape)
admin.site.register(color)
admin.site.register(region)
admin.site.register(size)

