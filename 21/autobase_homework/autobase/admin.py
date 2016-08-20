from django.contrib import admin
from .models import Auto, Manufacturer, Warehouse, Buyer, Orders


@admin.register(Auto)
class AutoAdmin(admin.ModelAdmin):
    list_display = ('name', 'manufacturer', 'body', 'year')
    date_hierarchy = 'year'
    list_filter = ('name', 'manufacturer', 'body')
    fieldsets = (
            (None, {
                'fields': ('name', 'manufacturer', 'body')
            }),
            ('Топливные характеристики', {
                'classes': ('wide',),
                'fields': ('fuelType', 'fuelRate'),
            }),
            ('Характеристики двигателя', {
                'classes': ('wide',),
                'fields': ('engineVolume', 'enginePower'),
            }),
             ('Прочие характеристики', {
                 'fields': ('gearbox', 'year')
             }),
        )


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('brand', 'country')
    list_filter = ('brand', 'country')


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'price')


@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('name', 'lastname', 'email', 'phone')


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('goods', 'buyer', 'amount', 'time')
    list_filter = ('time', )
