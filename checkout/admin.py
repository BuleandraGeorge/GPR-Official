from django.contrib import admin
from .models import Order, lineitem

class lineitemAdmin(admin.TabularInline):
    model = lineitem
    readonly_fields=('lineitem_total',)

class orderAdmin(admin.ModelAdmin):
    inlines = (lineitemAdmin,)

admin.site.register(Order, orderAdmin)
# Register your models here.
