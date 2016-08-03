from django.contrib import admin
from .models import Auto, Manufacturer


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
