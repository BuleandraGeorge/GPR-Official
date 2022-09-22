from django.contrib import admin

from .models import wine, color, grape, region, size, size_details, translation


class wineQuantityAvailableDetailsAdmin(admin.TabularInline):
    model = size_details

class wineTranslations(admin.TabularInline):
    model = translation

class wineAdmin(admin.ModelAdmin):
    inlines = [
        wineQuantityAvailableDetailsAdmin,
        wineTranslations
    ]
    list_display = (
        'name',
        'color',
        'region',
        'grape',
        'first_time_listed',
        'rating',
        'image',
    )
    ordering = ('first_time_listed',)


admin.site.register(wine, wineAdmin)
admin.site.register(grape)
admin.site.register(color)
admin.site.register(region)
admin.site.register(size)

