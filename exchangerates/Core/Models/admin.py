from django.contrib import admin

from .models.currencyrates import CurrencyRates
from .models.сurrencies import Currencies

class AdminCurrencies(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'symbol')

admin.site.register(Currencies, AdminCurrencies)

class AdminCurrencyRates(admin.ModelAdmin):
    list_display = ('id', 'currency', 'date_added', 'actual_date', 'price_usd')

admin.site.register(CurrencyRates, AdminCurrencyRates)
